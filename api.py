# -*- coding: utf-8 -*-
from requests import get

STATS_ITEMS = (
    ("Absolute running time", "مدت زمان اجرا"),
    ("cpu time", "مدت پردازش"),
    ("memory peak", "مقدار رم مصرف شده"),
    ("absolute service time", "مدت استفاده از سرویس"),
    ("Compilation time", "مدت زمان کامپایل"),
    ("sec", "ثانیه"),
    (", ", "\n> ")
)


class RextesterApi:

    @staticmethod
    def __replace(code: str):
        for rep in STATS_ITEMS:
            code = code.replace(*rep)
        return code

    @staticmethod
    def __message(interpreter: int, user: str, code: str, result: str, stats: str) -> str:
        return f"""
*مفسر :* پایتون {interpreter}
*کاربر :* {user}\n
*کد ارسال شده :* \n
`{code}`\n
*نتیجه :* \n
`{result}`\n
*منابع مصرف شده :* \n
`{stats}`
        """

    def rextester_api(self, lang_id, code, uid, username):
        resp = get(f"https://rextester.com/rundotnet/api?LanguageChoice={lang_id}&Program={code}").json()

        """Response List"""
        errors = resp['Errors']
        result = resp['Result']
        stats = f"> {self.__replace(resp['Stats'])}"

        if errors is not None:
            return self.__message(3 if lang_id == 24 else 2,
                                  f"[{uid}](tg://user?id={username})",
                                  code if len(code) < 500 else 'Telegram limited character size',
                                  errors,
                                  stats
                                  )
        else:
            return self.__message(3 if lang_id == 24 else 2,
                                  f"[{uid}](tg://user?id={username})",
                                  code if len(code) < 500 else 'Telegram limited character size',
                                  result,
                                  stats
                                  )
