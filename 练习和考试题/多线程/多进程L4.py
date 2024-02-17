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
    print("-------------main over----------")
    # 结果只有task1会在main结束后继续执行。
