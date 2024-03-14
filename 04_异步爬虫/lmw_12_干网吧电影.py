# 1.拿到视频页面源代码
# 2.从视频页面源代码得到对应的iframe，提取iframe中的src
# 3.从对应的src的对应页面源代码中，解析出真正的M3U8文件地址
# 4.下载第一层M3U8，从第一层M3U8中解析出第二层的地址
# 5.下载第二层M3U8，从第二层中解析出每一个TS文件的路径，启动协程任务
# 6.对TS文件进行解密
# 7.对TS文件进行合并，还原MP4文件

import requests
from lxml import etree
import re


def get_page_source(url):
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 109.0.0.0Safari / 537.36"
    }
    resp =requests.get(url=url,headers=headers)
    resp.encoding="utf-8"
    return resp.text

def get_first_m3u8(url):
    # 1.拿到视频页面源代码
    # 2.从视频页面源代码找到一层m3u8的 url 地址
    page_source= get_page_source(url)
    obj = re.compile(r'var vid="(?P<first_m3u8_url>.*?)";',re.S)
    first_m3u8_url= obj.search(page_source).group("first_m3u8_url")
    return first_m3u8_url

def get_m3u8_file(first_m3u8_url):
    print(first_m3u8_url)
    first_m3u8 = get_page_source(first_m3u8_url)


#
# https://chaoren.sc2yun.com/play.php?v=https://vip.lz-cdn9.com/20220519/10250_96e93019/index.m3u8
# https://vip.lz-cdn9.com/20220519/10250_96e93019/index.m3u8


def main():
    url = "https://mjw21.com/dp/NDY4OS0xLTA=.html"
    first_m3u8_url = get_first_m3u8(url)
    get_m3u8_file(first_m3u8_url)

if __name__ == '__main__':
    main()