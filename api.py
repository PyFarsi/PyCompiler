#!./venv/Scripts python
# -*- coding: utf-8 -*-
# CREATED BY https://t.me/rezafd

from requests import post, get
from urllib.parse import quote_plus

DICT_STATUS_ID = {
    4: 'Wrong Answer',
    5: 'Time Limit Exceeded',
    6: 'Compilation Error',
    7: 'Runtime Error (SIGSEGV)',
    8: 'Runtime Error (SIGXFSZ)',
    9: 'Runtime Error (SIGFPE)',
    10: 'Runtime Error (SIGABRT)',
    11: 'Runtime Error (NZEC)',
    12: 'Runtime Error (Other)',
    13: 'Internal Error',
    14: 'Exec Format Error'
}

def rexter(code: str, v: int, is_fa: bool, cid, really_cid) -> str:
    rexter_url_api = 'https://rextester.com/rundotnet/api?LanguageChoice=%i&Program=%s'
    url_code = quote_plus(code)
    rsp = get(rexter_url_api % (24 if v != 5 else 5, url_code))
    print(rsp)
    dic = eval(rsp.text.replace('null', 'None').replace("false", "False").replace("true", "True"))
    return analyze_result(dic, v, is_fa, cid, code, really_cid)


def analyze_result(dic: dict, v, is_fa: bool, cid, code, really_cid) -> str:
    stats = dic['Stats'].replace('Absolute running time', 'مدت زمان اجرا').replace('cpu time',
                                                                                   'مدت پردازش پردازنده').replace(
        'memory peak', 'مقدار رم مصرف شده').replace('absolute service time', 'مدت استفاده از سرویس').replace('sec',
                                                                                                             'ثانیه')
    stats = '> ' + stats.replace(', ', '\n> ')
    warn_en = '\n\n*Warnings:*\n%s' % dic['Warnings']
    warn_fa = '\n\nاخطارها:\n%s' % dic['Warnings']
    if dic['Errors'] is not None:
        result_code = dic['Errors']
        msg = """
*مفسر :‌* Python {}

*کاربر : *{}

*کد : *
`{}`

*نتیجه : * 
`{}`
""".format(3 if v!=5 else 2, f'[{cid}](tg://user?id={really_cid})', code if len(code) < 500 else 'Telegram limit', result_code)
        return msg
    else:
        result_code = dic['Result']
        msg = """
*مفسر :‌* Python {}

*کاربر : *{}

*کد : *
`{}`

*نتیجه : * 
`{}`
""".format(3 if v!=5 else 2, f'[{cid}](tg://user?id={really_cid})', code if len(code) < 500 else 'Telegram limit', result_code)
        return msg
