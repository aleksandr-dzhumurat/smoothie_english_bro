import asyncio
import glob as glob_module
import os
import random
import tempfile
import time

from telegram import __version__ as TG_VER

from ai_agent import dialog_router, english_to_russian
from gemini_adapter import generate_speech
from utils import load_json, get_file_path, dump_json
from db import save_message, get_message_by_id, setup_database

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
from telegram import ForceReply, InputFile, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, MessageReactionHandler


TOKEN = os.environ['TG_BOT_TOKEN']
quiz_file_path = get_file_path('quiz_db.json')
quiz_db = load_json(quiz_file_path)
keys = list(quiz_db.keys())
print(f'Num keys {len(keys)}')
message_history = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Use /help for help",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    response = [
        "Send me a phrase  with errors in english (or event in russian). I will make you phrase to sound smothier!"
    ]
    for i in response:
        await update.message.reply_text(i)

async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /quiz is issued."""
    user_id = update.effective_user.id
    random_k = random.choice(keys)
    # if not user_id in message_history:
    #     message_history[user_id] = random_k
    response = quiz_db[random_k]
    msg1 = await update.message.reply_text(response)
    await save_message(
        message_id=msg1.message_id,
        chat_id=msg1.chat_id,
        user_id=context.bot.id,
        message_text=response,
        reply_to_message_id=update.message.message_id
    )
    time.sleep(15)
    msg2 = await update.message.reply_text(random_k)
    await save_message(
        message_id=msg2.message_id,
        chat_id=msg2.chat_id,
        user_id=context.bot.id,
        message_text=random_k,
        reply_to_message_id=update.message.message_id
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

        quiz_db.update({message_data['message_text']: english_to_russian(message_data['message_text'])})
        dump_json(quiz_db, quiz_file_path)
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

    # Save user's message
    await save_message(
        message_id=update.message.message_id,
        chat_id=update.message.chat_id,
        user_id=user_tg.id,
        message_text=update.message.text
    )

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
                reply_to_message_id=update.message.message_id
            )


def main() -> None:
    """Start the bot."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quiz", quiz_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_dialog))
    
    application.add_handler(MessageReactionHandler(handle_reaction))
    loop.run_until_complete(setup_database())
    
    
    application.run_polling(
        allowed_updates=["message", "edited_message", "channel_post", 
                        "edited_channel_post", "message_reaction"],
    )

if __name__ == "__main__":
    main()
