import time

import requests
import os
from bs4 import BeautifulSoup

# get请求，传入参数 url，获取对应页面的源代码
class Request_get():
    def __init__(self,url):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        self.url = url

    def response(self):
        self.resp = requests.get(url = self.url,headers=self.headers)
        return self.resp


if __name__ == '__main__':
    url = "https://www.gushicimingju.com/novel/sanguoyanyi/"
    R = Request_get(url)
    resp = R.response()

    # 创建三国演义目录，用来存放爬取的内容
    if not os.path.exists("三国演义"):
       os.mkdir("三国演义")

    soup = BeautifulSoup(resp.text,"html.parser")
    li_lst = soup.find("ul",class_="content-left left-2-col").find_all("li")
    for li in li_lst:
        name = li.find("a").text
        href = url+li.find("a")["href"].lstrip("/novel/sanguoyanyi/")

        # 获取单章的页面源代码
        R_2 = Request_get(href)
        resp_1 = R_2.response()
        # print(resp_1.text)
        # 初始化，对单章页面源代码进行处理
        soup_2 = BeautifulSoup(resp_1.text,"html.parser")
        page = soup_2.find("div",class_="shici-content check-more").text
        with open("三国演义/"+name,"w",encoding="utf-8") as fp:
            fp.write(page)
        # print(f"{name},{href}")
        print(name+"\t下载完成！！")
        time.sleep(2)

    print("爬取完成！！！")
# https://www.gushicimingju.com/novel/sanguoyanyi/
# https://www.gushicimingju.com/novel/sanguoyanyi/361.html
# https://www.gushicimingju.com/novel/sanguoyanyi/novel/sanguoyanyi/361.html