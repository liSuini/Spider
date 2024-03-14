import json

import requests
url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

data = {
    "type":24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": "20"
}
resp = requests.get(url=url,headers=headers,params=data)
resp_obj = resp.json()

with open("豆瓣电影排行榜.json","w",encoding="utf-8") as f:
    json.dump(resp_obj,f,ensure_ascii=False)

print("爬取完成！！！")
resp.close()