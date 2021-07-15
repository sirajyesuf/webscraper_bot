from handlers.start import start_command_handler
from handlers.registration import add_channel_message_handler
from telegram.ext import Updater, updater
from handlers.startnow import start_now_command_handler
from dotenv import load_dotenv
import os
load_dotenv()


load_dotenv()
token = os.getenv('token')


def main():
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(add_channel_message_handler)
    dispatcher.add_handler(start_now_command_handler)
    updater.start_polling()
    print("working")
    updater.idle()


if __name__ == "__main__":
    main()
