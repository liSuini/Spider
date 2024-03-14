import aiohttp
import aiofile
import asyncio
import os


async def download(url):
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 109.0.0.0Safari / 537.36"
    }
    if not os.path.exists("优美图库"):
        os.mkdir("优美图库")
    file_name = url.split("/")[-1]
    print("下载开始",url)
    # 相当于requests
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as resp:
            # await resp.text() # =>resp.text
            content = await resp.content.read()  # => resp.content
            # 写入文件
            async with aiofile.async_open("优美图库/"+file_name,mode="wb") as fp:
                await fp.write(content)

    print("下载完成",url)

async def main():
    url_list=[
        "https://i1.huishahe.com/uploads/allimg/202203/9999/3091f0b07d.jpeg",
        "https://i1.huishahe.com/uploads/allimg/202205/9999/08a7a9fdda.jpg",
        "https://i1.huishahe.com/uploads/allimg/202205/9999/971d3fc855.jpg",
        "https://i1.huishahe.com/uploads/tu/201911/9999/95bb285000.jpg",
        "https://i1.huishahe.com/uploads/tu/201911/9999/f899e61d0e.jpg",
        "https://i1.huishahe.com/uploads/tu/201911/9999/2ed70a066e.jpg",
        "https://i1.huishahe.com/uploads/tu/201910/9999/e4e01a56fa.jpeg",
        "https://i1.huishahe.com/uploads/tu/201911/9999/c4c780ebba.jpg"
    ]
    tasks = []
    for url in url_list:
        task = asyncio.create_task(download(url))
        tasks.append(task)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
