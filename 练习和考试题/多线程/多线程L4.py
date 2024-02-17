import threading
import time

sum = 0


def add_one():
    global sum
    # 添加锁
    lock.acquire()
    for i in range(1000000):
        sum += 1
    lock.release()
    # 释放锁
    # 锁添加的位置也很有讲究，在本案例中 其实会导致数据冲突的是sum+=1这个动作。for循环是独立的迭代的，i并不会互相冲突。
    # 但是为什么不在for循环中增加锁，是因为这样做每个线程在处理一次累加后都需要加解锁一次，也就是3x100000次。严重影响性能。
    # 而放在for循环外，则代表每个线程在一次完成100000次循环前是不会解锁的，减少了加锁解锁的重复操作。减轻系统压力

    print(threading.current_thread().name, " : ", sum)


if __name__ == '__main__':
    # 数据冲突，在不加锁的情况下，可以看到三个线程的执行并不是平均的累加的。python3.9后优化了结果，但过程还是凌乱的。
    lock = threading.Lock()
    t1 = threading.Thread(target=add_one)
    t2 = threading.Thread(target=add_one)
    t3 = threading.Thread(target=add_one)
    t1.start()
    t2.start()
    t3.start()
    time.sleep(3)
    print(threading.current_thread().name, " : ", sum)
