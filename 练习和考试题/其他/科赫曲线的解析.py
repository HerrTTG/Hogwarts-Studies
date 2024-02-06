import turtle as t


def A():
    # n==0的特例
    t.fd(20)


def n1():
    # n==1时走进函数，先转角度，在执行n=n-1即n==0的特例封装A（）
    t.left(0)
    A()
    t.left(60)
    A()
    t.left(-120)
    A()
    t.left(60)
    A()


def n2():
    # n==2时走进函数，先转角度，在执行n=n-1即n==1的特例封装n1()
    t.left(60)
    n1()
    t.left(-120)
    n1()
    t.left(60)
    n1()


def n3():
    # n==2时走进函数，先转角度，在执行n=n-1即n==2的特例封装n2()
    t.left(60)
    n1()
    n2()
    t.left(-120)
    n1()
    n2()
    t.left(60)
    n1()
    n2()


def 三阶科赫():
    n1()
    n2()
    n3()


def 等边三角形雪花():
    三阶科赫()
    t.right(120)
    三阶科赫()
    t.right(120)
    三阶科赫()
    t.right(120)


def main():
    t.setup(600, 600)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.pensize(2)
    t.speed(0)
    等边三角形雪花()
    t.done()


main()
