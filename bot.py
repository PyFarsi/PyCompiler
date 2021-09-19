# -*- coding: utf-8 -*-
import json
import os
import re

import telegram
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from src.api import RextesterApi
from src.logger import Logger

rex = RextesterApi()
log = Logger()


def clang(bot, update):
    msg = "اوکی, لطفا کدی که به زبان CLang هست را برایم بفرستید"
    log.info("CLang Request.")
    bot.message.reply_text(msg)


def cpplang(bot, update):
    msg = "اوکی, لطفا کدی که به زبان CPlusPlus هست را برایم بفرستید"
    log.info("C++ Request.")
    bot.message.reply_text(msg)


def mysql(bot, update):
    msg = "اوکی, لطفا کدی که به زبان MySQL هست را برایم بفرستید"
    log.info("MySQL Request.")
    bot.message.reply_text(msg)


def sql_server(bot, update):
    msg = "اوکی, لطفا کدی که به زبان SQL Server هست را برایم بفرستید"
    log.info("SQL Server Request.")
    bot.message.reply_text(msg)


def psql(bot, update):
    msg = "اوکی, لطفا کدی که به زبان PostgreSQL هست را برایم بفرستید"
    log.info("PostgreSQL Request.")
    bot.message.reply_text(msg)


def python3(bot, update):
    msg = "اوکی, لطفا کدی که به زبان Python 3 هست را برایم بفرستید"
    log.info("Python 3 Request.")
    bot.message.reply_text(msg)

def golang(bot, update):
    msg = "اوکی, لطفا کدی که به زبان Go هست را برایم بفرستید"
    log.info("Golang Request.")
    bot.message.reply_text(msg)

def get_code(bot, update):
    msg = bot.message or bot.edited_message
    code = msg.text
    msg_reply = msg.reply_to_message.text
    cid = msg.from_user.first_name
    really_cid = msg.from_user.id
    callback_result(msg, code, msg_reply, cid, really_cid)


def callback_result(message, code, msg_reply, cid, really_cid):
    if (securityCheck(code) and ("اوکی, لطفا کدی که به زبان" in msg_reply)
            and "." not in msg_reply):
        message.reply_text(f"کتابخانه یا تابع استفاده شده در کد شما مجاز نیست!")
        return

    if msg_reply:
        if ("CLang" in msg_reply and ("اوکی, لطفا کدی که به زبان" in msg_reply)
                and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(6, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
        elif ("CPlusPlus" in msg_reply and ("اوکی, لطفا کدی که به زبان" in msg_reply)
              and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(7, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
        elif ("MySQL" in msg_reply
              and ("اوکی, لطفا کدی که به زبان" in msg_reply)
              and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(33, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
        elif ("SQL Server" in msg_reply
              and ("اوکی, لطفا کدی که به زبان" in msg_reply)
              and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(16, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
        elif ("PostgreSQL" in msg_reply
              and ("اوکی, لطفا کدی که به زبان" in msg_reply)
              and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(34, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
        elif ("Python 3" in msg_reply
              and ("اوکی, لطفا کدی که به زبان" in msg_reply)
              and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(24, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )
        
        elif ("Go" in msg_reply
              and ("اوکی, لطفا کدی که به زبان" in msg_reply)
              and "." not in msg_reply):
            message.reply_text(
                rex.rextester_api(20, code, cid, really_cid),
                parse_mode=telegram.ParseMode.MARKDOWN,
            )


def get_settings():
    if os.path.exists("./settings.json"):
        with open("./settings.json") as setting_file:
            setting = json.load(setting_file)

        return {
            "token": setting["token"],
            "proxy": setting["proxy"],
            "proxy_address": setting["proxy_address"],
        }
    raise Exception("settings.json not found.")

def securityCheck(code):
    if re.findall(r"(exec\(.*\))|(eval\(.*\))", code):
        return True
    
    filter_modules = ("os", "sys", "platform", "subprocess")
    filter_codes = [f"import {m}" for m in filter_modules] + [f"from {m}" for m in filter_modules]
    
    for fm in filter_codes:
        if fm in code:
            return True
    
    if "asyncio.subprocess" in code or "asyncio.create_subprocess_shell" in code:
        return True
    
    return False

if __name__ == "__main__":
    settings = get_settings()
    if settings["proxy"]:
        updater = Updater(
            settings["token"],
            use_context=True,
            request_kwargs={
                "proxy_url": f"socks5h://{settings['proxy_address']}"
            },
        )
    else:
        updater = Updater(settings["token"], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(
        MessageHandler(
            filters=(Filters.chat_type.groups & Filters.text & Filters.reply),
            callback=get_code,
        ))
    dp.add_handler(CommandHandler("py", python3, Filters.chat_type.groups))
    dp.add_handler(CommandHandler("c", clang, Filters.chat_type.groups))
    dp.add_handler(CommandHandler("cpp", cpplang, Filters.chat_type.groups))
    dp.add_handler(CommandHandler("mysql", mysql, Filters.chat_type.groups))
    dp.add_handler(
        CommandHandler("sqlsv", sql_server, Filters.chat_type.groups))
    dp.add_handler(CommandHandler("psql", psql, Filters.chat_type.groups))
    dp.add_handler(CommandHandler("go", golang, Filters.chat_type.groups))
    updater.start_polling()
    updater.idle()
