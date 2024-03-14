import asyncio
import time

async def fun1():
    print("我是任务1")
    # 在协程任务中，等待时不能使用 time.sleep（） 而应该使用协程函数中的等待await asyncio.sleep(1)
    await asyncio.sleep(1)
    print("任务1结束")

async def fun2():
    print("我是任务2")
    await asyncio.sleep(2)
    print("任务2结束")

async def fun3():
    print("我是任务3")
    await asyncio.sleep(3)
    print("任务3结束")

if __name__ == '__main__':
    start = time.time()
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()

    tasks = [
        f1,
        f2,
        f3
    ]
    asyncio.run(asyncio.wait(tasks))
    print(time.time()-start)

