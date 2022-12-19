import sys
import requests
import cloudscraper
import re
import random
import threading

welcometxt = """

Better Boxfresh Spammer
open README.md and enjoy :)
made by start#2434

"""
def headergen(cookie, url, name, content, avatar):
    header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,km-KH;q=0.4,km;q=0.3",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": f"simple={cookie} ;",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
  }
    body = {
    'device_uid':cookie,
    'slug': url.split('=')[-1],
    'uname': name,
    "avatar": avatar,
    "ios_user": "1",
    "content": content,
    "commit": "%E4%BB%A5%E4%B8%8B%E3%81%AB%E5%90%8C%E6%84%8F%E3%81%97%E3%81%A6%E8%B3%AA%E5%95%8F%E3%82%92%E3%81%8A%E3%81%8F%E3%82%8B"
  }
    return header, body


def boxfreshspammer(url, content, randstr):
    session = cloudscraper.CloudScraper()
    result = session.get(url).text
    if "random" in content:
        content = random.choice(txt)
    if randstr in ["y","yes"]:
        content += "\n" + "".join(random.choices("ABCDWFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=10))
    cookie = re.findall("{val = '.+';", result)[0].split("'")[1]
    avatar_png = re.findall('<input name="avatar" type="hidden" value=".+"/><input', result)[0].split(' ')[-1].split('"')[1]
    uname = re.findall('content=".+のBoxFreshです"/><meta name="twitter:card"',result)[0].split('"')[-4].replace('のBoxFreshです','')
    header, data = headergen(cookie, url, uname, content, avatar_png)
    r = session.post("https://boxfresh-jp.com/apppage.php",headers=header,data=data)
    if r.status_code in (200, 201, 305):
        print(f"送信が完了しました。\nInfomation:\ntoken: {cookie}\ntarget-name: {uname}")

print(welcometxt)
url = input('ターゲットのBoxfresh urlを入力してください。\n')
content = input('送りたいメッセージを入力してください。\nOption:\nrandom: boxfresh.txtの中を読み取り、１行をランダムに送信します。\nlist: 上記ファイルを上から順番に送信します。\n')

amount = int(input('送信したい回数を整数で入力してください。\n'))
randstr = input('ランダムな文字をメッセージ中に追加しますか？ [yes / no]\n')
if content == "list" or content == "random":
    try:
        with open("boxfresh.txt",encoding="utf-8") as f:
            txt = [i for i in f.read().splitlines() if i != None]
    except:
        print("txtファイルが見つかりませんでした。追加後、もう一度お試しください。")
        sys.exit()
if content == "list":
    for i in range(amount):
        for i in txt:
              threading.Thread(target=boxfreshspammer,args=(url, i, randstr)).start()
     #       boxfreshspammer(url, i, randstr)
else:
    for i in range(amount):
      #  boxfreshspammer(url, content, randstr)
      threading.Thread(target=boxfreshspammer,args=[url,content,randstr]).start()
