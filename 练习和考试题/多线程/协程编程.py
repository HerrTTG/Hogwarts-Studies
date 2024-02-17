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

# join是协程的启动方式而不是等待完成
# g1.join()
# g2.join()
# g3.join()


# 协程组 joinall 可以同时启动协程组中的task
# gs=[gevent.spawn(task) for i in range(5)]
# gevent.joinall(gs)


# 协程异步，类似于线程的无序执行。
# 异步的概念是虽然我只有一个人在执行这么多的任务，但是我可以选择性暂停某个任务，去执行一下其他任务
# 如我在切菜的同时 可能偶尔操作一下煮米饭的锅。亦可以去洗个筷子。然后在回来继续切菜。
# 没有多余的人(线程)帮我执行其他任务，都是我一个人，但执行的结果是可以凌乱的。而不是一定非要执行完某个才能开始下一个。
# 也就是说不是单步向下执行的。
g1 = gevent.spawn(task1, 5, "Python")
g2 = gevent.spawn(task1, msg="Hogwarts", n=5)
g3 = gevent.spawn(task1, n=5, msg="Hello")
gevent.joinall((g1, g2, g3))
