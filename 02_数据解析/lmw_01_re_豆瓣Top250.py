import re
import requests
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

fp = open("豆瓣top250.csv","w",encoding="utf-8")
obj = re.compile(r'<div class="item">.*?<em class="">(?P<num>.*?)</em>'
                 r'.*?<span class="title">(?P<title>.*?)</span>'
                 r'.*?<p class="">(?P<direct>.*?)&nbsp'
                 r'.*?<br>(?P<years>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<number>.*?)</span>'
                 r'.*?<span class="inq">(?P<comment>.*?)</span>', re.S)
for i in range(10):
    start = i *25
    param = {
        "start":start
    }
    resp = requests.get(url=url,headers=headers,params=param)
    page_source = resp.text

    # print(page_source)
    result = obj.finditer(page_source)
    for item in result:
        num = item.group("num")
        title = item.group("title")
        score = item.group("score")
        direct = item.group("direct").strip()
        years = item.group("years").strip()
        number = item.group("number")
        comment = item.group("comment")
        fp.write(f"{num},{title},{score},{direct},{years},{number},{comment}\n")


fp.close()
resp.close()

print("爬取完成")