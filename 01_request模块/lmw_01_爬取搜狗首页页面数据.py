import requests
url = "https://www.sogou.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
resp = requests.get(url=url,headers=headers)
page = resp.text
with open("sougou.html","w",encoding="utf-8") as f:
    f.write(page)
resp.close()
print(page)