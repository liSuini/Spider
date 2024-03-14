import requests

url ="https://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

proxy = {
    "http":"60.211.218.78:53281",
    "https":"60.211.218.78:53281"
}

resp = requests.get(url= url,headers=headers,proxies=proxy)
print(resp.text)

resp.close()