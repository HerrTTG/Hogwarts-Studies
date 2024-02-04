import threading
import time


# 跳舞任务
def task1():
    for i in range(5):
        print("跳舞中...")
        print(threading.current_thread())
        time.sleep(0.2)


# 唱歌任务
def task2():
    for i in range(5):
        print("唱歌中...")
        print(threading.current_thread())
        time.sleep(0.2)


def task():
    time.sleep(1)
    print(threading.current_thread().name)


g_list = list()


def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)


sum = 0


def add_one():
    global sum
    lock.acquire()
    for i in range(1000000):
        sum += 1
    lock.release()
    print(threading.current_thread().name, " : ", sum)


if __name__ == '__main__':
    # 线程守护和进程守护最大的区别。
    # 如果只单独设置一个线程守护，是无法退出主程序的。线程守护被杀死，触发条件是主线程退出。
    # 当t2没有被设置守护时，主程序要等待他，所以t1无法被杀死
    # print(threading.current_thread())
    # t1 = threading.Thread(target=task1,daemon=True)
    # t2 = threading.Thread(target=task2)
    # # t2.daemon = True
    # t1.start()
    # t2.start()
    # time.sleep(0.2)
    # print('main over')

    # 执行无序性
    # for i in range(5):
    #     t = threading.Thread(target=task)
    #     t.start()

    # 数据共享
    # add_data_Thread = threading.Thread(target=add_data)
    # read_data_Thread = threading.Thread(target=read_data)
    #
    # add_data_Thread.start()
    # add_data_Thread.join()
    # read_data_Thread.start()
    #
    # print("main:", g_list)

    # 数据的冲突混乱
    lock = threading.Lock()
    t1 = threading.Thread(target=add_one)
    t2 = threading.Thread(target=add_one)
    t3 = threading.Thread(target=add_one)
    t1.start()
    t2.start()
    t3.start()
    time.sleep(3)
    print(threading.current_thread().name, " : ", sum)
