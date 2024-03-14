from threading import Thread

def fun(name):
    for i in range(50):
        print(f"{name},{i}")

if __name__ == '__main__':
    # 在不使用多线程的情况下
    print("不使用多线程：")
    fun_1 = fun("周润发")
    fun_2 = fun("胡歌")
    fun_3 = fun("周杰伦")
    print("*"*100)
    # 创建线程
    print("使用多线程执行：")
    t_1 = Thread(target=fun,args=("周润发",))
    # t_1.start()
    # 在传递参数时，args后面传递的参数必须是元组类型，所以要在括号内再添加一个”，“
    t_2 = Thread(target=fun, args=("胡歌",))
    t_3 = Thread(target=fun, args=("周杰伦",))
    Thread(target=fun, args=("lalal",)).start()

    t_1.start()
    t_2.start()
    t_3.start()

    # 在使用多线程时，除了我们所定义的几个多线程以外，还有一个主线程。
    print("我是主线程————————————————————————————————————————————————————")
