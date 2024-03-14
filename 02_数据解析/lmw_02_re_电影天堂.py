import re
import requests

url = "https://www.dy2018.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

obj_1 = re.compile(r"2022必看热片.*?</ul>",re.S)
obj_2 = re.compile(r"<li><a href='(?P<add>.*?)' title=(?P<name>.*?)>",re.S)
obj_3 = re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<link_1>.*?)">',re.S)

resp = requests.get(url=url,headers=headers)
resp.encoding = "gb2312"
page_source = resp.text

# 抓取必看热片部分的页面代码
result_1 = re.findall(obj_1,page_source)

result_2 = re.finditer(obj_2,result_1[0])
for item in result_2:
    url_child =url+item.group("add")[1:]
    print(item.group("name")[1:-1])
    resp_2 = requests.get(url=url_child,headers=headers)
    resp_2.encoding = "gb2312"
    page_source_1 = resp_2.text

    result_3 = obj_3.finditer(page_source_1)
    for item_1 in result_3:
        print(item_1.group("link_1"))
    print("")

resp.close()