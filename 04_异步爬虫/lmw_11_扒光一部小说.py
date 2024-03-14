import aiohttp
import requests
import asyncio
import aiofile
import os
from lxml import etree

def get_every_chapter_url(url,headers):
    resp = requests.get(url=url,headers=headers)
    # print(resp.text)
    tree = etree.HTML(resp.text)
    href_lst = tree.xpath('//*[@id="section-list"]/li/a/@href')
    # print(href_lst)
    return href_lst

async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            page_source = await resp.text()
            tree = etree.HTML(page_source)
            title = tree.xpath("//div[@class='reader-main']//h1[@class='title']/text()")[0].strip()
            content = "\n".join(tree.xpath('//div[@class="content"]/text()')).replace("\n\xa0\xa0\xa0\xa0","")

            async with aiofile.async_open("三体/"+title+".txt","w",encoding="utf-8")as f:
                await f.write(content)
            print(title,"over!!!")

async def download(url_list):
    tasks = []
    for url in url_list:
        task = asyncio.create_task(download_one("https://www.zanghaihua.org/book/40626/"+url))
        tasks.append(task)

    await asyncio.wait(tasks)

def main():
    if not os.path.exists("三体"):
        os.mkdir("三体")
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 109.0.0.0Safari / 537.36"
    }
    url="https://www.zanghaihua.org/book/40626/"
    # 抓取页面源代码，得到每章小说的url地址
    url_list = get_every_chapter_url(url,headers)
    print(url_list)
    # 启动协程，爬取章节内容
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(download(url_list))


if __name__ == '__main__':
    main()