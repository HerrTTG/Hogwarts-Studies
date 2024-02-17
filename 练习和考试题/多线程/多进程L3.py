import multiprocessing
import os
import time


# 跳舞任务
def task():
    # 多进程执行同一个任务，可以用进程名来区分。
    for i in range(10):
        if multiprocessing.process.current_process().name == 'Process-1':
            print('run task1', os.getpid(), os.getppid())
        elif multiprocessing.process.current_process().name == 'Process-2':
            print('run task2', os.getpid(), os.getppid())
        time.sleep(0.2)


if __name__ == '__main__':
    # 多进程执行同一个任务，可以用进程名来区分。
    # 同属一个父进程，但是子进程不同。所以是同一个task在分别独立执行2次
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    print(os.getpid())
    p1.start()
    p2.start()
