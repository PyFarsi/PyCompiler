# -*- coding: utf-8 -*-
import os
import json

from src.api import RextesterApi

import telegram
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

rex = RextesterApi()


def set_en(bot, update):
    bot.message.reply_text('set en for language.')


def python2(bot, update):
    msg = 'اوکی, لطفا کدی که به زبان پایتون 2 هست را برایم بفرستید'
    bot.message.reply_text(msg)


def python3(bot, update):
    msg = 'اوکی, لطفا کدی که به زبان پایتون 3 هست را برایم بفرستید'
    bot.message.reply_text(msg)


def get_code(bot, update):
    msg = bot.message or bot.edited_message
    code = msg.text
    msg_reply = msg.reply_to_message.text
    cid = msg.from_user.first_name
    really_cid = msg.from_user.id
    callback_result(msg, code, msg_reply, cid, really_cid)


def callback_result(message, code, msg_reply, cid, really_cid):
    if "import os" in code and ('اوکی, لطفا کدی که به زبان' in msg_reply) and '.' not in msg_reply:
        message.reply_text("استفاده از کتابخانه os مجاز نیست.")
        
    if msg_reply:
        if 'پایتون 2' in msg_reply and ('اوکی, لطفا کدی که به زبان' in msg_reply) and '.' not in msg_reply:
            message.reply_text(rex.rextester_api(5, code, cid, really_cid), parse_mode=telegram.ParseMode.MARKDOWN)
        elif 'پایتون 3' in msg_reply and ('اوکی, لطفا کدی که به زبان' in msg_reply) and '.' not in msg_reply:
            message.reply_text(rex.rextester_api(24, code, cid, really_cid), parse_mode=telegram.ParseMode.MARKDOWN)


def get_settings():
    if os.path.exists('./settings.json'):
        with open("./settings.json") as setting_file:
            setting = json.load(setting_file)

        return {
            "token": setting['token'],
            "proxy": setting['proxy'],
            "proxy_address": setting['proxy_address']
        }

    else:
        raise Exception("setting.json not found.")


if __name__ == '__main__':
    settings = get_settings()
    if settings['proxy']:
        updater = Updater(settings['token'], use_context=True, request_kwargs={
            "proxy_url": f"socks5h://{settings['proxy_address']}"
        })
    else:
        updater = Updater(settings['token'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=(Filters.chat_type.groups & Filters.text & Filters.reply), callback=get_code))
    dp.add_handler(CommandHandler('python3', python3, Filters.chat_type.groups))
    dp.add_handler(CommandHandler('py3', python3, Filters.chat_type.groups))
    dp.add_handler(CommandHandler('python2', python2, Filters.chat_type.groups))
    dp.add_handler(CommandHandler('py2', python2, Filters.chat_type.groups))
    updater.start_polling()
    updater.idle()
