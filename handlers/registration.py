from typing import Text
from telegram import ext
import telegram
from telegram.ext import MessageHandler, Filters
from models.channel import update_channel
import time


def addChannel(update, context):
    channel = update.message.forward_from_chat
    if(check_for_the_bot_is_administorator(channel, context)):
        result = update_channel(update.message.forward_from_chat)
        msg = "channel registered successfully" if result == 1 else "channel deleted successfully"
        msg2 = '''' if you ready to start posting news from voa startup and technology archive 
        pls use the the command /startnow timeinterval delay_b/n_posts_time
        exampale /startnow 60 10
        the time interval and  the delay_b/n_posts_time shoud be in min. from above   60 means every 1hr
        '''

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=msg
        )
        time.sleep(3)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=msg2)

    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="pls first add the bot as administorartor"
        )


add_channel_message_handler = MessageHandler(
    Filters.forwarded, addChannel)


def check_for_the_bot_is_administorator(channel, context):
    try:
        context.bot.get_chat_administrators(channel.id)
        return 1
    except (telegram.error.BadRequest, telegram.error.Unauthorized):
        return 0
