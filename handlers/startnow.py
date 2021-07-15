from telegram import ext
from telegram.ext import CommandHandler
from telegram.ext import(commandhandler, Filters)
from models.channel import store_time_interval_delay_time, get_channel, get_urls, store_url
from services.voa_scraper import Voa
import time


def startNow(update, context):
    l = context.args
    try:
        time_interval = int(float(l[0])*60)
        delay_time = int(float(l[1])*60)
        if(validate(time_interval, delay_time)):
            store_time_interval_delay_time(time_interval, delay_time)
            channel = get_channel()
            cxt = {
                'channel': channel,
                'delay_time': delay_time
            }
            context.job_queue.run_repeating(
                scraper, time_interval, context=cxt, name=str(channel['title']))

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')


start_now_command_handler = CommandHandler('startnow', startNow)


def validate(time_interval, delay_time):
    if(time_interval < 0 or delay_time < 0):
        return 0
    return 1


def scraper(context):
    ctx = context.job.context

    old_urls = get_urls()
    scraper = Voa()
    html = scraper.today()
    posts = html.find('.vertical-list__item')
    l = []
    new_urls = []
    for i in posts:
        a = i.find('.teaser')
        l.append(a)
    for i in l:
        a = i[0].find('a')[1].attrs['href']
        new_urls.append(scraper.BASE_URL1+a)
    newpost_urls = []

    for i in new_urls:
        if(i not in old_urls):
            newpost_urls.append(i)
    print(len(newpost_urls))
    if(len(newpost_urls)):
        store_url(newpost_urls)
        sendPost(context, newpost_urls, ctx)


def sendPost(context, posts, ctx):
    print(ctx)
    posts.reverse()
    for i in posts:
        context.bot.send_message(
            chat_id=ctx['channel']['id'],
            text=f"{i}",
            disable_web_page_preview=False

        )
        time.sleep(ctx['delay_time'])
