import requests
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
words = input("请输入要查询的单词：")
data ={
    "kw":words
}
resp =requests.post(url=url,headers=headers,params=data)
response = resp.json()
for i in response["data"]:
    print(i)

resp.close()