import multiprocessing
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


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task1, name='Process1')
    p2 = multiprocessing.Process(target=task2, name='Process2')
    p3 = multiprocessing.Process(target=task3, name='Process3', args=('xq',))
    print('main:', multiprocessing.process.current_process())
    p1.start()
    p2.start()
    # join为进程同步，当前进程执行结束后，才会执行下一条语句
    p1.join()
    p2.join()
    p3.start()
