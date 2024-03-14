import requests
from pyquery import pyquery
import os
import time


if __name__ == '__main__':
    url = "https://www.gushicimingju.com/novel/shuihuzhuan/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    if not os.path.exists("水浒传"):
        os.mkdir("水浒传")

    resp = requests.get(url=url,headers=headers)
    py = pyquery.PyQuery(resp.text)
    li_lst = py("ul.content-left.left-2-col li").items()
    for li in li_lst:
        name = li.text()
        href = url+li("a").attr("href").split("/")[-1]
        resp_1 = requests.get(url=href,headers=headers)
        py_1 = pyquery.PyQuery(resp_1.text)
        p = py_1("p").text()
        with open("水浒传/"+name,"w",encoding="utf-8") as f:
            f.write(p)
        print(name+"\tover!!!!")
        time.sleep(1)

    print("all over!!!")


    resp.close()