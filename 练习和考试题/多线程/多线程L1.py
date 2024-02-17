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


if __name__ == '__main__':
    # 线程守护和进程守护最大的区别。
    # 如果只单独设置一个线程守护，是无法退出主程序的。线程守护被杀死，触发条件是主线程退出。
    # 当t2没有被设置守护时，主程序要等待他，所以t1无法被杀死
    print(threading.current_thread())
    # t1设置了线程守护,但t2没有
    t1 = threading.Thread(target=task1, daemon=True)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    time.sleep(0.2)
    print('------------main over--------------')
    # 结果是t1虽然线程守护了，但是t2没有守护。所以主线程不会为此而退出。导致守护线程认为不需要关闭t1
    # 所以线程的守护必须所有子线程都设置才有用
