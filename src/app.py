import asyncio
import glob as glob_module
import html as html_lib
import os
import random
import tempfile
import time

import markdown as md_lib
from bs4 import BeautifulSoup, NavigableString

from telegram import __version__ as TG_VER

from ai_agent import dialog_router, english_to_russian
from gemini_adapter import generate_speech, generate_text
from prompts import generate_prompt
from utils import load_jsonl, get_file_path, append_jsonl
from db import save_message, get_message_by_id, setup_database, get_session, set_session_state, get_messages_by_session

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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters, MessageReactionHandler


TG_MAX_LEN = 4096


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
message_history = {}


MAIN_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("quiz", callback_data="quiz"),
     InlineKeyboardButton("case", callback_data="case")]
])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Choose:", reply_markup=MAIN_KEYBOARD)


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "quiz":
        await quiz_command(update, context)
    elif query.data == "case":
        await case_command(update, context)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    response = [
        "Send me a phrase  with errors in english (or event in russian). I will make you phrase to sound smothier!"
    ]
    for i in response:
        await update.message.reply_text(i)

async def _send_reply(update: Update, text: str, **kwargs):
    """Send a reply via message or callback query."""
    if update.message:
        return await update.message.reply_text(text, **kwargs)
    elif update.callback_query:
        return await update.callback_query.message.reply_text(text, **kwargs)


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /quiz is issued."""
    user_id = update.effective_user.id
    session = await get_session(user_id)
    await set_session_state(session['session_id'], 'quiz')

    entry = random.choice(quiz_db)
    rus_text = entry['rus']
    eng_text = entry['eng']
    msg1 = await _send_reply(update, rus_text)
    await save_message(
        message_id=msg1.message_id,
        chat_id=msg1.chat_id,
        user_id=context.bot.id,
        message_text=rus_text,
        session_id=session['session_id']
    )
    time.sleep(15)
    msg2 = await _send_reply(update, eng_text)
    await save_message(
        message_id=msg2.message_id,
        chat_id=msg2.chat_id,
        user_id=context.bot.id,
        message_text=eng_text,
        session_id=session['session_id']
    )
    await set_session_state(session['session_id'], 'translate')

async def case_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a case study session."""
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

        new_entry = {'eng': message_data['message_text'], 'rus': english_to_russian(message_data['message_text'])}
        quiz_db.append(new_entry)
        append_jsonl(new_entry, quiz_file_path)
        print(f"Message text that was reacted to: {message_data['message_text']} with {reaction_emoji}")

        text = message_data['message_text']
        with tempfile.TemporaryDirectory() as tmpdir:
            output_base = os.path.join(tmpdir, 'speech')
            await asyncio.get_event_loop().run_in_executor(None, generate_speech, text, output_base)
            audio_files = sorted(glob_module.glob(f"{output_base}_*"))
            friendly_name = '🔊 ' + '_'.join(text.split()[:4]) + '.wav'
            for audio_path in audio_files:
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

    # Route "quiz"/"case" text to the corresponding commands
    if update.message.text.strip().lower() in ('quiz', 'case'):
        cmd = update.message.text.strip().lower()
        if cmd == 'quiz':
            await quiz_command(update, context)
        else:
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
    elif session_state == 'case':
        history = await get_messages_by_session(session['session_id'], limit=2)
        history.append(update.message.text)
        user_prompt = "\n".join(history)
        response = md_to_tg_html(generate_text(generate_prompt(), user_prompt))
        for chunk in split_html(response):
            message = await update.message.reply_text(chunk, parse_mode='HTML')
            await save_message(
                message_id=message.message_id,
                chat_id=message.chat_id,
                user_id=context.bot.id,
                message_text=chunk,
                reply_to_message_id=update.message.message_id,
                session_id=session['session_id']
            )
        await set_session_state(session['session_id'], 'translate')


def main() -> None:
    """Start the bot."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quiz", quiz_command))
    application.add_handler(CommandHandler("case", case_command))
    application.add_handler(CallbackQueryHandler(handle_buttons, pattern="^(quiz|case)$"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_dialog))
    
    application.add_handler(MessageReactionHandler(handle_reaction))
    loop.run_until_complete(setup_database())
    
    
    application.run_polling(
        allowed_updates=["message", "edited_message", "channel_post",
                        "edited_channel_post", "message_reaction", "callback_query"],
    )

if __name__ == "__main__":
    main()
