import requests
from lxml import etree
from urllib import parse
from multiprocessing import Process,Queue
from concurrent.futures import ThreadPoolExecutor
import os
# 进程1 爬取每个图片的url地址

# 进程2 根据进程1 的地址下载图片


def Get_src(url,q):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    resp = requests.get(url=url,headers=headers)
    resp.encoding = "utf-8"
    et = etree.HTML(resp.text)
    href_lst = et.xpath('//div[@class = "item_list infinite_scroll"]//div[@class="item_b clearfix"]//a/@href')
    for href in href_lst:
        child_href = parse.urljoin(url,href)
        resp1 = requests.get(url=child_href,headers=headers)
        resp1.encoding = "utf-8"
        et2 =etree.HTML(resp1.text)
        src = et2.xpath('//div[@class="big-pic"]/a/img/@src')[0]
        q.put(src)
        print(src+"进入队列")
    q.put("over")

def Get(q):
    with ThreadPoolExecutor(5) as t:
        for i in range(2,10):
            url =f"https://www.umei.cc/weimeitupian/keaitupian/index_{i}.htm"
            t .map(Get_src,[url],[q])

def Downpic(url):
    resp = requests.get(url=url)
    resp.encoding = "utf-8"
    name = url.split("/")[-1]
    with open("优美图库/"+name,"wb") as f:
        f.write(resp.content)
    print(name+"下载完成")

def Download(q):
    with ThreadPoolExecutor(5) as t:
        while 1:
            url = q.get()
            if url != "over":
                t.submit(Downpic,url)
            else:
                break


if __name__ == '__main__':

    if not os.path.exists("优美图库"):
        os.mkdir("优美图库")
    q = Queue()
    p1 = Process(target=Get,args=(q,))
    p2 = Process(target=Download,args=(q,))
    p1.start()
    p2.start()
    print("over!!!")
