from threading import Thread


# 继承Thread父类
class Mythread(Thread):
    def __init__(self,name):
        super(Mythread, self).__init__()
        self.name=name

    def run(self):
        for i in range(50):
            print(f"{self.name},{i}")

if __name__ == '__main__':
    t1 =Mythread("周杰伦")
    t2 = Mythread("胡歌")
    t3 = Mythread("周润发")

    t1.start()
    t2.start()
    t3.start()
