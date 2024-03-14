import requests

url = "https://www.sogou.com/web"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
name = input("请输入要查询的内容：")
data = {
    "query":name
}
resp = requests.get(url=url,headers=headers,params=data)
with open(name+".html","w",encoding="utf-8") as f:
    f.write(resp.text)
resp.close()
print(resp.text)
