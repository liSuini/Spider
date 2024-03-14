import requests
import os
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    resp =requests.get(url=url,headers=headers)
    et = etree.HTML(resp.text)
    title = et.xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]/h1/text()")
    article = et.xpath("/html/body/div[3]/div/div[1]/div[1]/div[2]/p//text()")
    t="".join(title)
    s = "".join(article).replace("\r\r","\r")
    with open(f"西游记/{t}.text","w",encoding="utf-8") as f:
        f.write(s)
    print(t,"over!!")

if __name__ == '__main__':
    if not os.path.exists("西游记"):
        os.mkdir("西游记")
    with ThreadPoolExecutor(5) as t:
        for i in range(1,102):
            num = 480+i
            url =f"https://www.gushicimingju.com/novel/xiyouji/{num}.html"
            t.submit(download,url)
    print("all over!!!")