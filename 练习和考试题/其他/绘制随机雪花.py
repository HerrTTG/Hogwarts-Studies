import turtle as t 
import random

t.setup(800,600)
t.hideturtle()
t.speed(0)
t.delay(0)


def koch(size, n):
    # size 直线长度，阶数n
    if n == 0:
        t.fd(size)
    else:
        for i in [0, 60, -120, 60]:
            t.left(i)
            koch(size / 3, n - 1)


def snowflake(size):
    level = 3
    for i in range(level):
        koch(size, level)
        t.right(360 / level)


colors=["lightblue","lightcyan","lavender"]

for i in range(100):
    x=random.randint(-400,400)
    y=random.randint(-300,300)
    size=random.randint(10,20)
    color=random.choice(colors)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.pensize(size//4)
    snowflake(size)
    t.seth(random.randint(0,360))
t.hideturtle()
t.done()
