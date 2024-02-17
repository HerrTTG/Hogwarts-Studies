import threading
import time


def task():
    time.sleep(1)
    print(threading.current_thread().name)


if __name__ == '__main__':
    # 线程并发的无序性。每次执行的循序都是不一样的
    for i in range(5):
        t = threading.Thread(target=task)
        t.start()
