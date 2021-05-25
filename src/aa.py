import requests

cookies = {
    'ASP.NET_SessionId': 'qlmtoi1yh5s1fdsjcwgfmjtj',
    '__utmc': '178476455',
    '__gads': 'ID=fed7a3c47ff8d12d:T=1621928418:S=ALNI_MZubu5mJyusqTaW0Gx_eTomknyLSw',
    '__utma': '178476455.434738208.1621928405.1621928405.1621929689.2',
    '__utmz': '178476455.1621929689.2.2.utmcsr=google^|utmccn=(organic)^|utmcmd=organic^|utmctr=(not^%^20provided)',
    '__utmt': '1',
    '__utmb': '178476455.1.10.1621929689',
    'cto_bundle': 'juwS019wbDVXYTFBT1IwJTJGSWJTN0c5JTJCdFNuZUl6VU10WWhLT0VDUmdtRmFKQURIa1FiblBqTjRmdHAyVW1jMjFTaUNobHAxSVI4alVwd0N5ayUyRjBJWiUyQkdWMHMlMkIxcHh2VndzYiUyRlFHSUVjYmdlWHE3bE92MjhEbHUlMkJ6bVhFJTJGc0VielJoNEN6bkdnREp6YXl3enl4QWRkQWh2WTF3JTNEJTNE',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '^\\^',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://rextester.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://rextester.com/l/go_online_compiler',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
}

data = {
  'LanguageChoiceWrapper': '20',
  'EditorChoiceWrapper': '1',
  'LayoutChoiceWrapper': '1',
  'Program': '''package main 

import "fmt" 

func main() { fmt.Println("hello world")
i := 0
for i < 1000 { i++ } 
fmt.Println(i)}''',
  'CompilerArgs': '-o a.out source_file.go',
  'Input': '',
  'ShowWarnings': 'false',
  'Privacy': '',
  'PrivacyUsers': '',
  'Title': '',
  'SavedOutput': '',
  'WholeError': '',
  'WholeWarning': '',
  'StatsToSave': '',
  'CodeGuid': '',
  'IsInEditMode': 'False',
  'IsLive': 'False'
}

response = requests.post('https://rextester.com/rundotnet/Run', headers=headers, cookies=cookies, data=data)
print(response.text)