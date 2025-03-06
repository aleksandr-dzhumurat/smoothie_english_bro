import json
import os
import random
import time

from telegram import __version__ as TG_VER

from ai_agent import dialog_router

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
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


def load_quiz_db(quize_db_path):
    if not os.path.exists(quize_db_path):
        return {}
    with open(quize_db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

TOKEN = os.environ['TG_BOT_TOKEN']
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
quiz_file_path = os.path.join(current_dir, 'quiz_db.json')
quiz_db = load_quiz_db(quiz_file_path)
keys = list(quiz_db.keys())
print(f'Num keys {len(keys)}')


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

message_history = {}

async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /quiz is issued."""
    user_id = update.effective_user.id
    random_k = random.choice(keys)
    # if not user_id in message_history:
    #     message_history[user_id] = random_k
    response = quiz_db[random_k]
    await update.message.reply_text(response)
    time.sleep(15)
    await update.message.reply_text(random_k)

async def bot_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_tg = update.effective_user
    user = {'user_id': user_tg.id, 'user_name': user_tg.username}
    print(user)
    if user['user_id'] in message_history:
        response = message_history[user['user_id']]
        del message_history[user['user_id']]
        await update.message.reply_text(response)
    else:
        bot_response = dialog_router(update.message.text, user)
        for line in bot_response['answer'].split('\n'):
            if len(line) > 0 and '>' in line:
                await update.message.reply_text(line)


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quiz", quiz_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_dialog))
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
