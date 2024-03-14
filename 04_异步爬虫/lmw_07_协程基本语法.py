# 协程语法
import asyncio

async def fun():
    print("我是函数！！")

if __name__ == '__main__': #程序入口
    # 协程对象想要执行，必须借助于 event_loop

    f = fun()
    # 拿到事件循环
    event_loop = asyncio.get_event_loop()
    # 执行协程对象，直到该对象内容执行完毕
    event_loop.run_until_complete(f)
    # asyncio.run(f)
    