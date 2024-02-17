import threading
import time

g_list = list()


def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)


if __name__ == '__main__':
    # 数据共享
    add_data_Thread = threading.Thread(target=add_data)
    read_data_Thread = threading.Thread(target=read_data)

    add_data_Thread.start()
    add_data_Thread.join()
    read_data_Thread.start()
    print("main:", g_list)
    # 可以看到子线程之间数据是共享的，甚至主线程都能获取到
