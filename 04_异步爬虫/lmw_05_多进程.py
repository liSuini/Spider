from multiprocessing import Process


def func(name):
    for i in range(100):
        print(f"我是{name},{i}")

if __name__ == '__main__':
    p1 = Process(target=func,args=("周杰伦",))
    p2 = Process(target=func, args=("李连杰",))

    p1.start()
    p2.start()