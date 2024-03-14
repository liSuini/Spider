import time
import requests
from bs4 import BeautifulSoup
import os
import csv


fp = open("优美图库.csv","w",encoding="utf-8")
aim_url = {}
url = "https://www.umei.cc/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# 爬取首页的源代码
resp = requests.get(url=url,headers=headers)
resp.encoding = "utf-8"
first_page = resp.text

# 初始化bs4对象
bs4_page = BeautifulSoup(first_page,"lxml")
li_lst_01 = bs4_page.find_all("li",class_="nav-li on")

# 遍历 li标签列表，获取每个模块下的自主题
for li in li_lst_01:
    a_lst_01 = li.find("div", class_="sonnav").find_all("a")
    for a in a_lst_01:
        type = a.text
        type_url = url.rstrip("/")+a["href"]
        aim_url[type] = type_url

    #     fp.write(f"{type},{type_url}\n")
    # fp.write("\n")
print("可爬取的图片类型有：")
print(aim_url.keys())
type_name = input("请输入你要爬取的主题：")

# 创建相应主题的子目录
if not os.path.exists("优美图库/"+type_name):
    os.mkdir("优美图库/"+type_name)

# 爬取子类型的网页源代码
resp_2 = requests.get(aim_url[type_name],headers=headers)
resp_2.encoding = "utf-8"

# 初始化
type_page= BeautifulSoup(resp_2.text,"html.parser")
div_list = type_page.find_all("div",class_="item masonry_brick")

# 遍历div标签，获得每张图片的地址
for div in div_list:
    picture_name =div.find("div",class_="title").text
    picture_url = url.rstrip("/")+div.find("div",class_="title").find("a")["href"]

    # 访问每张图片的地址，获得图片
    resp_3 = requests.get(url=picture_url,headers=headers)
    resp_3.encoding = "utf-8"

    #初始化
    picture_page = BeautifulSoup(resp_3.text,"html.parser")
    picture_last = picture_page.find("div",class_ = "big-pic").find("img")["src"]

    # 获取图片
    resp_4 = requests.get(url=picture_last,headers=headers)

    # 本地化存储
    with open("优美图库/"+type_name+"/"+picture_name+".jpg","wb") as fp_1:
        fp_1.write(resp_4.content)

    print(picture_name+"爬取完成！！！")
    time.sleep(2)

    # print(f'{picture_name},{picture_url}\n')

# 结束
fp.close()
resp.close()
resp_2.close()
print("所有图片爬取完成！！！")

