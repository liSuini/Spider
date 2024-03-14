from concurrent.futures import ThreadPoolExecutor
import time

def func(name,t):
    time.sleep(t)
    print(f"我是{name}")
    return name


def fn(res):
    print(res.result())

if __name__ == '__main__':
    with ThreadPoolExecutor(5) as t:
        result = t.map(func,["周杰伦","胡歌","周星驰"],[2,1,3])
        # result 是一个生成器
        print(result)
        for r in result:
            print(r)
        # 此时返回的结果为任务封装时，三个参数的顺序即：周杰伦，胡歌，周星驰，并不是按照时间先后
        # map 返回顺序与封装相同。
