from telegram.ext import (
    MessageHandler,
    CommandHandler,
    Filters
)

from services.voa_scraper import Voa
import time
import telegram


def start(update, context):
    start_msg = '''
    welcome to voawebscraper bot.this bot help you to post news from voa to your channel or group\n\n
    pls first add the bot to your group or channel then forward any message to the  bot to register.
    '''
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=start_msg
    )




start_command_handler = CommandHandler('start', start)
