import asyncio


async def fun1():
    print("我是任务1")
    # 在协程任务中，等待时不能使用 time.sleep（） 而应该使用协程函数中的等待await asyncio.sleep(1)
    await asyncio.sleep(1)
    print("任务1结束")
    return "任务1的返回值"

async def fun2():
    print("我是任务2")
    await asyncio.sleep(2)
    print("任务2结束")
    return "任务2的返回值"

async def fun3():
    print("我是任务3")
    await asyncio.sleep(3)
    print(1/0)
    print("任务3结束")
    return "任务3的返回值"

async def main():
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()

    tasks = [
        asyncio.create_task(f2),
        asyncio.create_task(f1),
        asyncio.create_task(f3)
    ]
    # done, pending =await asyncio.wait(tasks)
    # for rest in done:
    #     print(rest.result())
    # print(pending)
    result =await asyncio.gather(*tasks,return_exceptions=True)
    # *tasks  动态传参
    for i in result:
        print(i)

if __name__ == '__main__':
    asyncio.run(main())