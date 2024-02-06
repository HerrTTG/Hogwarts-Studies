# 递归函数的练习，函数koch的解析看科赫曲线的解析.py
import turtle as t


def koch(size, n):
    # size 直线长度，阶数n
    if n == 0:
        t.fd(size)
    else:
        for i in [0, 60, -120, 60]:
            t.left(i)
            koch(size / 3, n - 1)


def three():
    level = 3
    for i in range(level):
        koch(400, level)
        t.right(360 / level)


def main():
    t.setup(600, 600)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.pensize(2)
    t.speed(0)
    three()
    t.done()


main()
