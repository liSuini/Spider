import requests

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
params = {
    "op":"keyword"
}
data = {
    "cname": "",
    "pid": "",
    "keyword": input("请输入要查询的城市："),
    "pageIndex": 1,
    "pageSize": 10
}
resp = requests.post(url=url,headers=headers,params=params,data=data)

with open("肯德基餐厅位置.text","w",encoding="utf-8") as fp:
        fp.write(resp.text)
print("爬取完成！！！")
resp.close()