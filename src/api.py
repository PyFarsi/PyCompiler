from requests import get

STATS_ITEMS = (
    ("Absolute running time", "مدت زمان اجرا"),
    ("cpu time", "مدت پردازش"),
    ("memory peak", "مقدار رم مصرف شده"),
    ("absolute service time", "مدت استفاده از سرویس"),
    ("Compilation time", "مدت زمان کامپایل"),
    ("Execution time", "مدت زمان اجرا"),
    ("rows selected", "ردیف های انتخاب شده"),
    ("rows affected", "ردیف های تحت تاثیر"),
    ("sec", "ثانیه"),
    ("absolute running time", "مدت زمان در حال اجرا"),
    (", ", "\n> "),
)

COMPILER_ARGS = {
    "c": "-Wall -std=gnu99 -O2 -o a.out source_file.c",
    "cpp": "-Wall -std=c++14 -O2 -o a.out source_file.cpp",
    "go": "-o a.out source_file.go"
}


class RextesterApi:
    @staticmethod
    def __replace(code: str):
        for rep in STATS_ITEMS:
            code = code.replace(*rep)
        return code

    @staticmethod
    def __message(interpreter: str, user: str, code: str, result: str,
                  stats: str) -> str:
        return f"""
*زبان :* _{interpreter}_
*کاربر :* {user}\n
*کد ارسال شده :* \n
`{code}`\n
*نتیجه :* \n
`{result}`\n
*منابع مصرف شده :* \n
`{stats}`

.
        """

    def rextester_api(self, lang_id: int, code: str, uid: str, username: str):
        if lang_id == 6:
            resp = get(
                f"https://rextester.com/rundotnet/api?LanguageChoice={lang_id}"
                f"&Program={code}"
                f"&CompilerArgs={COMPILER_ARGS['c']}"
            ).json()
        elif lang_id == 7:
            resp = get(
                f"https://rextester.com/rundotnet/api?LanguageChoice={lang_id}"
                f"&Program={code}"
                f"&CompilerArgs={COMPILER_ARGS['cpp']} "
            ).json()
        elif lang_id == 20:
            resp = get(
                f"https://rextester.com/rundotnet/api?LanguageChoice={lang_id}"
                f"&Program={code}"
                f"&CompilerArgs={COMPILER_ARGS['go']}"
            ).json()
        else:
            resp = get(
                f"https://rextester.com/rundotnet/api?LanguageChoice={lang_id}"
                f"&Program={code}"
            ).json()

        """Response List"""
        errors = resp["Errors"]
        result = resp["Result"]
        stats = f"> {self.__replace(resp['Stats'])}"

        lang = None
        if lang_id == 6:
            lang = "C"
        elif lang_id == 7:
            lang = "++C"
        elif lang_id == 33:
            lang = "MySQL"
        elif lang_id == 16:
            lang = "SQL Server"
        elif lang_id == 34:
            lang = "PostgreSQL"
        elif lang_id == 24:
            lang = "Python 3"
        elif lang_id == 20:
            lang = "Go"

        if errors is not None:
            return self.__message(
                lang,
                f"[{uid}](tg://user?id={username})",
                code if len(code) < 500 else "Telegram limited character size",
                errors,
                stats,
            )
        return self.__message(
            lang,
            f"[{uid}](tg://user?id={username})",
            code if len(code) < 500 else "Telegram limited character size",
            result,
            stats,
        )
