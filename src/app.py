import asyncio
import html as html_lib
import os
import random
import tempfile
import time
import uuid

import markdown as md_lib
from bs4 import BeautifulSoup, NavigableString
from google.genai.errors import ServerError

from telegram import __version__ as TG_VER

from ai_agent import dialog_router, english_to_russian
from gemini_adapter import generate_speech, generate_text
from prompts import generate_prompt, generate_interview_prompt, generate_ideal_answer_prompt
from utils import load_jsonl, get_file_path, append_jsonl, QuestionsDB
from db import save_message, get_message_by_id, setup_database, get_session, set_session_state, get_messages_by_session, set_interview_question
from grammar import ANSWER_PATTERN, grammar_answer, grammar_command, load_grammar_store, stats_command

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InputFile, ReplyKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters, MessageReactionHandler


TG_MAX_LEN = 4096
WAITING_FOR_LLM = "⏳ waiting for LLM"


def _is_case_skip(text: str) -> bool:
    return text.strip().casefold() in {'idk', '?'}


def split_html(text, limit=TG_MAX_LEN):
    """Split text into chunks not exceeding limit characters."""
    chunks = []
    while len(text) > limit:
        split_at = text.rfind('\n', 0, limit)
        if split_at == -1:
            split_at = limit
        chunks.append(text[:split_at])
        text = text[split_at:].lstrip('\n')
    if text:
        chunks.append(text)
    return chunks


def md_to_tg_html(text):
    def process(node):
        if isinstance(node, NavigableString):
            return html_lib.escape(str(node))
        tag = node.name
        inner = ''.join(process(child) for child in node.children)
        if tag in ('strong', 'b'):
            return f'<b>{inner}</b>'
        elif tag in ('em', 'i'):
            return f'<i>{inner}</i>'
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            return f'<b>{inner}</b>\n'
        elif tag == 'p':
            return f'{inner}\n\n'
        elif tag in ('ul', 'ol'):
            return inner
        elif tag == 'li':
            return f'• {inner}\n'
        elif tag == 'code':
            return f'<code>{inner}</code>'
        elif tag == 'pre':
            return f'<pre>{inner}</pre>'
        elif tag == 'hr':
            return '\n'
        elif tag == 'blockquote':
            return f'<blockquote>{inner}</blockquote>'
        elif tag == 'a':
            return f'<a href="{html_lib.escape(node.get("href", ""))}">{inner}</a>'
        return inner

    html = md_lib.markdown(text, extensions=['fenced_code'])
    soup = BeautifulSoup(html, 'html.parser')
    return ''.join(process(child) for child in soup.children).strip()


TOKEN = os.environ['TG_BOT_TOKEN']
quiz_file_path = get_file_path('quiz_db.jsonl')
quiz_db = load_jsonl(quiz_file_path)
print(f'Num entries {len(quiz_db)}')
try:
    questions_db = QuestionsDB.from_md()
except (OSError, ValueError) as e:  # a missing file or duplicate headings shouldn't stop the whole bot
    print(f'Interview questions not loaded: {e}')
    questions_db = QuestionsDB()
print(f'Num interview questions {len(questions_db)}')
message_history = {}


QUIZ_LABEL = "🎲 Quiz"
CASE_LABEL = "💬 Case"
GRAMMAR_LABEL = "📖 Grammar"
STATS_LABEL = "📊 Stats"

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [[QUIZ_LABEL, CASE_LABEL], [GRAMMAR_LABEL], [STATS_LABEL]],
    resize_keyboard=True,
    is_persistent=True,
)

WELCOME_MESSAGE = (
    "👋 <b>Welcome to Smoothie English Bot!</b>\n\n"
    "I'll help you practice business English and prepare for interviews.\n\n"
    "<b>Here is what you can do:</b>\n"
    "• 💬 <b>Polish your English:</b> Just send me any phrase (in English or Russian), and I'll suggest smoother corporate alternatives.\n"
    "• 🎯 <b>/quiz:</b> Translate a Russian prompt into English, or reply with idk or ? to reveal the answer.\n"
    "• 💬 <b>/case:</b> Practice a stand-up scenario or behavioral interview questions with AI feedback.\n"
    "• 📖 <b>/grammar:</b> Answer a multiple-choice grammar question and see the explanation.\n"
    "• 📊 <b>/stats:</b> See your grammar score and accuracy.\n"
    "• ⭐ <b>Save & Listen:</b> React with an emoji to any bot message to save it to your quiz and hear voice pronunciation.\n\n"
    '▶️ <a href="https://youtu.be/Djn4ZaWM2xM">Watch on YouTube</a>\n\n'
    "Choose a mode below or send me a phrase:"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    session = await get_session(update.effective_user.id)
    await set_session_state(session['session_id'], 'translate')
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=MAIN_KEYBOARD, parse_mode='HTML')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=MAIN_KEYBOARD, parse_mode='HTML')

async def _send_reply(update: Update, text: str, **kwargs):
    """Send a reply via message or callback query."""
    if update.message:
        return await update.message.reply_text(text, **kwargs)
    elif update.callback_query:
        return await update.callback_query.message.reply_text(text, **kwargs)


async def _send_html_reply(update: Update, context: ContextTypes.DEFAULT_TYPE, session: dict, html: str) -> None:
    """Send Telegram HTML in chunks of up to 4096 chars, saving every message to the session."""
    for chunk in split_html(html):
        message = await update.message.reply_text(chunk, parse_mode='HTML')
        await save_message(
            message_id=message.message_id,
            chat_id=message.chat_id,
            user_id=context.bot.id,
            message_text=chunk,
            reply_to_message_id=update.message.message_id,
            session_id=session['session_id']
        )


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the Russian prompt and wait for the user's next reply."""
    if not quiz_db:
        await _send_reply(update, "No quiz phrases are available yet.")
        return
    session = await get_session(update.effective_user.id)

    entry = random.choice(quiz_db)
    rus_text = entry['rus']
    message = await _send_reply(update, f"{rus_text}\n\nReply with your English translation, or send idk or ? to see the answer.")
    await set_session_state(session['session_id'], 'quiz', quiz_answer=entry['eng'])
    await save_message(
        message_id=message.message_id,
        chat_id=message.chat_id,
        user_id=context.bot.id,
        message_text=rus_text,
        session_id=session['session_id']
    )


async def reveal_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE, session: dict) -> None:
    """Reveal the saved translation after an attempt or a skip."""
    answer = session.get('quiz_answer')
    if answer is None:
        await _send_reply(update, "There's no active quiz question. Tap Quiz to start a new one.")
        await set_session_state(session['session_id'], 'translate')
        return

    message = await _send_reply(update, answer)
    await save_message(
        message_id=message.message_id,
        chat_id=message.chat_id,
        user_id=context.bot.id,
        message_text=answer,
        reply_to_message_id=update.message.message_id,
        session_id=session['session_id']
    )
    await set_session_state(session['session_id'], 'translate')

async def case_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a practice session: a random stand-up case or an interview question."""
    if len(questions_db) > 0 and random.random() < 0.5:
        await ask_interview_question(update, context)
        return

    user_id = update.effective_user.id
    session = await get_session(user_id)
    await set_session_state(session['session_id'], 'case')

    response = md_to_tg_html(generate_text(generate_prompt(), "Start a new stand-up warm-up session. Introduce the scene and ask the first question."))
    for chunk in split_html(response):
        msg1 = await _send_reply(update, chunk, parse_mode='HTML')
        await save_message(
            message_id=msg1.message_id,
            chat_id=msg1.chat_id,
            user_id=context.bot.id,
            message_text=chunk,
            session_id=session['session_id']
        )


async def ask_interview_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask a random question from behavioral_answers.md; the next message is scored."""
    if len(questions_db) == 0:
        await _send_reply(update, "No interview questions are loaded.")
        return
    asked = context.user_data.setdefault('asked_interview_ids', set())
    try:
        question = questions_db.sample(exclude_ids=asked)
    except ValueError:  # every question was asked already, so start a new round
        asked.clear()
        question = questions_db.sample()
    asked.add(question.id)

    session = await get_session(update.effective_user.id)
    await set_session_state(session['session_id'], 'interview')
    await set_interview_question(session['session_id'], question.id)

    question_html = f"🎤 <b>{html_lib.escape(question.title)}</b>"
    if question.hint:
        question_html += f"\n\n<b>Hint:</b> {html_lib.escape(question.hint)}"
    msg = await _send_reply(update, question_html, parse_mode='HTML')
    await save_message(
        message_id=msg.message_id,
        chat_id=msg.chat_id,
        user_id=context.bot.id,
        message_text=question.title,
        session_id=session['session_id']
    )


async def score_interview_answer(update: Update, context: ContextTypes.DEFAULT_TYPE, session: dict) -> None:
    """Score the answer, reveal the prepared ideal answer, then go back to translate mode."""
    question = questions_db.get(session.get('interview_question_id'))
    if question is None:
        await update.message.reply_text("I lost track of your interview question. Send /case to get a new one.")
    else:
        if not _is_case_skip(update.message.text):
            user_prompt = (
                f"Question: {question.title}\n\n"
                f"Ideal answer:\n{question.ideal_answer}\n\n"
                f"Answer:\n{update.message.text}"
            )
            feedback = await asyncio.to_thread(generate_text, generate_interview_prompt(), user_prompt)
            await _send_html_reply(update, context, session, md_to_tg_html(feedback))
        ideal = f"💡 <b>Ideal answer</b>\n\n{md_to_tg_html(question.ideal_answer)}"
        await _send_html_reply(update, context, session, ideal)
    await set_interview_question(session['session_id'], None)
    await set_session_state(session['session_id'], 'translate')


async def handle_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle when a user reacts to a bot message."""
    if hasattr(update, 'message_reaction') and hasattr(update.message_reaction, 'new_reaction'):
        if update.message_reaction.new_reaction:
            for reaction in update.message_reaction.new_reaction:
                if hasattr(reaction, 'emoji'):
                    reaction_emoji = reaction.emoji
                    break
    print(f'You are reacted with {reaction_emoji}')
    message_id = update.message_reaction.message_id
    chat_id = update.message_reaction.chat.id
    print(f"Debug: Searching for message_id {message_id} in chat {chat_id} in database...")
    message_data = await get_message_by_id(message_id, chat_id)
    if message_data:
        print(f"Debug: Found message data: {message_data}")
        # Print the text of the message that was replied to
        if message_data.get('reply_to_message_id'):
            replied_message = await get_message_by_id(message_data['reply_to_message_id'], chat_id)
            if replied_message:
                print(f"User replied to: {replied_message['message_text']}")
            else:
                print(f"Replied-to message {message_data['reply_to_message_id']} not found in DB for chat {chat_id}")
        else:
            print("This message was not a reply to anything recorded in our DB.")

        new_entry = {'id': str(uuid.uuid4()), 'eng': message_data['message_text'], 'rus': english_to_russian(message_data['message_text'])}
        quiz_db.append(new_entry)
        append_jsonl(new_entry, quiz_file_path)
        print(f"Message text that was reacted to: {message_data['message_text']} with {reaction_emoji}")

        text = message_data['message_text']
        with tempfile.TemporaryDirectory() as tmpdir:
            output_base = os.path.join(tmpdir, 'speech')
            await context.bot.send_message(chat_id=chat_id, text=WAITING_FOR_LLM)
            audio_path = await asyncio.to_thread(generate_speech, text, output_base)
            if audio_path:
                friendly_name = '🔊 ' + '_'.join(text.split()[:4]) + os.path.splitext(audio_path)[1]
                with open(audio_path, 'rb') as audio_file:
                    await context.bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file, filename=friendly_name))
    else:
        print(f"Debug: No message found in database with ID {message_id}. Was this message sent before the bot was updated?")


async def bot_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_tg = update.effective_user
    user = {'user_id': user_tg.id, 'user_name': user_tg.username}
    print(user)

    session = await get_session(user_tg.id)
    session_state = session['session_state']
    print(f"Session state: {session_state}")

    # Save user's message
    await save_message(
        message_id=update.message.message_id,
        chat_id=update.message.chat_id,
        user_id=user_tg.id,
        message_text=update.message.text,
        session_id=session['session_id']
    )

    # Accept the keyboard labels and the original plain-text shortcuts.
    cmd = update.message.text.strip().casefold()
    if cmd in ('quiz', QUIZ_LABEL.casefold()):
        await quiz_command(update, context)
        return
    if cmd in ('case', CASE_LABEL.casefold(), '💼 case'):
        await case_command(update, context)
        return

    if session_state == 'translate':
        bot_response = dialog_router(update.message.text, user)
        for line in bot_response['answer'].split('\n'):
            if len(line) > 0:
                message = await update.message.reply_text(line)
                message_text = line[2:] if line.startswith('> ') else line
                await save_message(
                    message_id=message.message_id,
                    chat_id=message.chat_id,
                    user_id=context.bot.id,
                    message_text=message_text,
                    reply_to_message_id=update.message.message_id,
                    session_id=session['session_id']
                )
    elif session_state == 'quiz':
        await reveal_quiz_answer(update, context, session)
    elif session_state == 'case':
        scenario = await get_messages_by_session(session['session_id'], limit=1, user_id=context.bot.id)
        user_prompt = "\n".join(scenario)
        if not _is_case_skip(update.message.text):
            user_prompt += f"\n\nAnswer:\n{update.message.text}"
            feedback = await asyncio.to_thread(generate_text, generate_prompt(), user_prompt)
            await _send_html_reply(update, context, session, md_to_tg_html(feedback))
        # a generated case has no prepared answer, so ask Gemini for the ideal one
        waiting_message = await update.message.reply_text(WAITING_FOR_LLM)
        ideal_prompt = generate_ideal_answer_prompt()
        for attempt in range(2):
            try:
                ideal_answer = await asyncio.to_thread(generate_text, ideal_prompt, user_prompt)
                break
            except ServerError as exc:
                if exc.code != 503:
                    raise
                if attempt == 0:
                    await asyncio.sleep(1)
                else:
                    await waiting_message.edit_text(
                        "Gemini is busy. Send ? again in a moment to get the ideal answer."
                    )
                    return
        ideal = f"💡 <b>Ideal answer</b>\n\n{md_to_tg_html(ideal_answer)}"
        await _send_html_reply(update, context, session, ideal)
        await set_session_state(session['session_id'], 'translate')
    elif session_state == 'interview':
        await score_interview_answer(update, context, session)


def main() -> None:
    """Start the bot."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = Application.builder().token(TOKEN).build()
    application.bot_data['grammar_store'] = load_grammar_store()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quiz", quiz_command))
    application.add_handler(CommandHandler("case", case_command))
    application.add_handler(CommandHandler("grammar", grammar_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(MessageHandler(filters.Text([GRAMMAR_LABEL]) | filters.Regex(r"(?i)^\s*grammar\s*$"), grammar_command))
    application.add_handler(MessageHandler(filters.Text([STATS_LABEL]) | filters.Regex(r"(?i)^\s*stats\s*$"), stats_command))
    application.add_handler(CallbackQueryHandler(grammar_answer, pattern=ANSWER_PATTERN))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_dialog))
    
    application.add_handler(MessageReactionHandler(handle_reaction))
    loop.run_until_complete(setup_database())
    
    
    application.run_polling(
        allowed_updates=["message", "edited_message", "channel_post",
                        "edited_channel_post", "message_reaction", "callback_query"],
    )

if __name__ == "__main__":
    main()
