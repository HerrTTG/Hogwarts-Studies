import multiprocessing
import os
import time


# 跳舞任务
def task1():
    for i in range(5):
        print("跳舞中...")
        print(multiprocessing.process.current_process())
        time.sleep(0.2)


# 唱歌任务
def task2():
    for i in range(5):
        print("唱歌中...")
        print(multiprocessing.process.current_process())
        time.sleep(0.2)


def task3(name):
    for i in range(5):
        print(name)
        print(multiprocessing.process.current_process())
        time.sleep(0.2)


def task():
    # 多进程执行同一个任务，可以用进程名来区分。
    for i in range(10):
        if multiprocessing.process.current_process().name == 'Process-1':
            print('run task1', os.getpid(), os.getppid())
        elif multiprocessing.process.current_process().name == 'Process-2':
            print('run task2', os.getpid(), os.getppid())
        time.sleep(0.2)


g_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)


if __name__ == '__main__':
    # p1 = multiprocessing.Process(target=task1, name="myprocess1")
    # p2 = multiprocessing.Process(target=task2)
    # p3 = multiprocessing.Process(target=task3,args=('xq',))

    # print('main:',multiprocessing.process.current_process())
    # p1.start()
    # p2.start()
    # #join为进程同步，当前进程执行结束后，才会执行下一条语句
    # p1.join()
    # p2.join()
    # p3.start()

    # 多进程执行同一个任务，可以用进程名来区分。
    # p1=multiprocessing.Process(target=task)
    # p2=multiprocessing.Process(target=task)
    # print(os.getpid())
    # p1.start()
    # p2.start()

    # #主进程不会等待子进程结束，而是在p1p2开始执行后立刻执行下一条语句 打印main over
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)
    p3 = multiprocessing.Process(target=task3, args=('xq',))

    print('main:', multiprocessing.process.current_process())
    p1.start()
    # p2设置了demon 主进程结束就会自动关闭p2对象的进程。而P1没有设置，会继续执行
    p2.daemon = True
    p2.start()
    p3.start()
    time.sleep(0.2)
    # p3 对象手动杀死进程
    p3.terminate()
    print("main over")

    # 进程之间数据独立，哪怕是全局变量。add的进程写入全局变量的list不能被父进程和其他进程所读取到。
    # add_data_process = multiprocessing.Process(target=add_data)
    # read_data_process = multiprocessing.Process(target=read_data)
    #
    # add_data_process.start()
    # add_data_process.join()
    # read_data_process.start()
    #
    # print("main:", g_list)
