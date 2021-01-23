#!./venv/Scripts/python
# -*- coding: utf-8 -*-
# CREATED BY https://t.me/rezafd

import os

import telegram

from api import *
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler


def set_en(bot, update):
    global is_fa
    is_fa = False
    bot.message.reply_text('set en for language.')

def python2(bot, update):
    en = 'اوکی, لطفا کدی که به زبان پایتون 2 هست را برایم بفرستید'
    bot.message.reply_text(en)


def python3(bot, update):
    en = 'اوکی, لطفا کدی که به زبان پایتون 3 هست را برایم بفرستید'
    bot.message.reply_text(en)


# def python3_file(bot, update):
#     doc = bot.message.reply_to_message.document
#     if doc is None or doc.file_name.split('.')[-1].lower() != 'py':
#         return
#     download_file(bot, doc)
#     with open('./catch/%s' % doc.file_name, 'r', encoding='utf-8') as file:
#         code = file.read()
#         file.close()
#     os.remove('./catch/%s' % doc.file_name)
#     print_result(bot, code, 'اوکی, لطفا کدی که به زبان پایتون 3 هست را برایم بفرستید')


# def python2_file(bot, update):
#     doc = bot.message.reply_to_message.document
#     if doc is None:
#         return
#     download_file(bot, doc)
#     with open('./catch/%s' % doc.file_name, 'r', encoding='utf-8') as file:
#         code = file.read()
#         file.close()
#     os.remove('./catch/%s' % doc.file_name)
#     print_result(bot, code, 'اوکی, لطفا کدی که به زبان پایتون 2 هست را برایم بفرستید')

# def download_file(bot, doc):
#     newFile = bot.get_file(doc.file_id)
#     newFile.download('./catch/%s' % doc.file_name)


def get_code(bot, update):
    msg = bot.message or bot.edited_message
    code = msg.text
    msg_reply = msg.reply_to_message.text
    cid = msg.from_user.first_name
    really_cid = msg.from_user.id
    print_result(msg, code, msg_reply, cid, really_cid)


def print_result(message, code, msg_reply, cid, really_cid):
    if 'import os' in code and 'پایتون' in msg_reply and ('اوکی, لطفا کدی که به زبان' in msg_reply):
        message.reply_text('*خطا:*\n`%s`' % '''File "source_file.py", line 1
    Import os
            ^
SyntaxError: invalid syntax''', parse_mode=telegram.ParseMode.MARKDOWN)
        return
    if msg_reply:
        if 'پایتون 2' in msg_reply and ('اوکی, لطفا کدی که به زبان' in msg_reply) and '.' not in msg_reply:
            message.reply_text(rexter(code, 5, is_fa, cid, really_cid), parse_mode=telegram.ParseMode.MARKDOWN)
        elif 'پایتون 3' in msg_reply and ('اوکی, لطفا کدی که به زبان' in msg_reply) and '.' not in msg_reply:
            message.reply_text(rexter(code, 24, False, cid, really_cid), parse_mode=telegram.ParseMode.MARKDOWN)


if __name__ == '__main__':
    is_fa = False
    if not os.path.exists('./catch'):
        os.mkdir('./catch')
    updater = Updater("1102486182:AAEgVpqIr-h4yw9nMYCTbioIsE-cUDuVh6k", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=(Filters.chat_type.groups & Filters.text & Filters.reply), callback=get_code))
    dp.add_handler(CommandHandler('python3', python3, Filters.chat_type.groups))
    dp.add_handler(CommandHandler('py3', python3, Filters.chat_type.groups))
    dp.add_handler(CommandHandler('python2', python2, Filters.chat_type.groups))
    dp.add_handler(CommandHandler('py2', python2, Filters.chat_type.groups))
    # dp.add_handler(CommandHandler('python3_file', python3_file, (Filters.chat_type.groups & Filters.reply)))
    # dp.add_handler(CommandHandler('py3_file', python3_file, (Filters.chat_type.groups & Filters.reply)))
    # dp.add_handler(CommandHandler('python2_file', python2_file, (Filters.chat_type.groups & Filters.reply)))
    # dp.add_handler(CommandHandler('pyf2', python2_file, (Filters.chat_type.groups & Filters.reply)))
    # dp.add_handler(CommandHandler('py2_file', python2_file, (Filters.chat_type.groups & Filters.reply)))
    updater.start_polling()
    updater.idle()


