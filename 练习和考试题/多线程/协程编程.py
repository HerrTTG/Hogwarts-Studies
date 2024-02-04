from gevent import monkey

monkey.patch_all()
import gevent
import random


def task():
    for i in range(1, 3):
        print(i, gevent.getcurrent())
        # 协程切换
        gevent.sleep(0.001)


def task1(n, msg):
    for i in range(1, n + 1):
        print(gevent.getcurrent(), f"第 {i} 次输出 {msg}")
        gevent.sleep(random.random())


# 启动方法
# g1 = gevent.spawn(task)
# g2 = gevent.spawn(task)
# g3 = gevent.spawn(task)
# g1.join()
# g2.join()
# g3.join()


# 协程组 joinall 可以同时启动协程组中的task
# gs=[gevent.spawn(task) for i in range(5)]
# gevent.joinall(gs)


# 协程异步
g1 = gevent.spawn(task1, 5, "Python")
g2 = gevent.spawn(task1, msg="Hogwarts", n=5)
g3 = gevent.spawn(task1, n=5, msg="Hello")
gevent.joinall((g1, g2, g3))
