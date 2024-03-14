import re
import requests
import csv

import time


fp = open("social_data.csv","w",encoding="utf-8")
url = "https://networkrepository.com/soc.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
obj = re.compile(r'<tr class="success hrefRow tooltips".*?&nbsp; <a href="(?P<download>.*?)".*?</tr>',re.S)

resp = requests.get(url= url,headers= headers)
page = resp.text
result = obj.finditer(page)
for item in result:
    url_1 = item.group("download")
    fp.write(f"{url_1}\n")
resp.close()
fp.close()
print("爬取完成")