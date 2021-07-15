import json
import re


def read():
    with open("models/channel.json", 'r') as f:
        data = json.load(f)
        return data


def write(payload):
    with open("models/channel.json", 'w') as f:
        json.dump(payload, f, indent=3)


def update_channel(channel):
    if(not get_channel()):
        store_channel(channel)
        return 1
    else:
        delete_channel()
        return 2


def store_channel(payload):
    channel = {
        "title": payload.title,
        "username": payload.username,
        "id": payload.id

    }

    data = read()
    data['channel'] = channel
    write(data)


def store_time_interval_delay_time(time_interval, delay_time):
    data = read()
    data['time_interval'] = time_interval
    data['delay_time'] = delay_time
    write(data)


def get_time_interval():
    return read()['time_interval']


def get_channel():
    return read()['channel']


def delete_channel():
    data = read()
    data['channel'] = 0
    write(data)
    return 1


def store_url(urls):
    data = read()
    data['urls'] = urls
    write(data)
    return 1


def get_urls():
    return read()['urls']
