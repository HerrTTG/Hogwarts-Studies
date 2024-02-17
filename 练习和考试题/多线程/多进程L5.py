import multiprocessing
import time


def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)


g_list = list()

if __name__ == '__main__':
    # 进程之间数据独立，哪怕是全局变量。add的进程写入全局变量的list不能被父进程和其他进程所读取到。
    add_data_process = multiprocessing.Process(target=add_data)
    read_data_process = multiprocessing.Process(target=read_data)

    add_data_process.start()
    add_data_process.join()
    read_data_process.start()

    print("main:", g_list)
# 结果就是其他进程读取不到,甚至main这个父进程也读取不到
