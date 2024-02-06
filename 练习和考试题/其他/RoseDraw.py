#RoseDraw.py
import turtle as t
import random
# 定义一个曲线绘制函数
def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))

# 绘制花朵形状
def drawflower(s):
    t.begin_fill()
    t.circle(200*s,30)
    DegreeCurve(60, 50*s)
    t.circle(200*s,30)
    DegreeCurve(4, 100*s)
    t.circle(200*s,50)
    DegreeCurve(50, 50*s)
    t.circle(350*s,65)
    DegreeCurve(40, 70*s)
    t.circle(150*s,50)
    DegreeCurve(20, 50*s, -1)
    t.circle(400*s,60)
    DegreeCurve(18, 50*s)
    t.fd(250*s)
    t.right(150)
    t.circle(-500*s,12)
    t.left(140)
    t.circle(550*s,110)
    t.left(27)
    t.circle(650*s,100)
    t.left(130)
    t.circle(-300*s,20)
    t.right(123)
    t.circle(220*s,57)
    t.end_fill()

# 绘制花枝形状
def drawspray(s):
    t.left(120)
    t.fd(280*s)
    t.left(115)
    t.circle(300*s,33)
    t.left(180)
    t.circle(-300*s,33)
    DegreeCurve(70, 225*s, -1)
    t.circle(350*s,104)
    t.left(90)
    t.circle(200*s,105)
    t.circle(-500*s,63)
    t.penup()
    t.goto(170*s,-30*s)
    t.pendown()
    t.left(160)
    DegreeCurve(20, 2500*s)
    DegreeCurve(220, 250*s, -1)

def drawleaves(s):
    # 绘制一个绿色叶子
    t.fillcolor('green')
    t.penup()
    t.goto(670*s,-180*s)
    t.pendown()
    t.right(140)
    t.begin_fill()
    t.circle(300*s,120)
    t.left(60)
    t.circle(300*s,120)
    t.end_fill()
    t.penup()
    t.goto(180*s,-550*s)
    t.pendown()
    t.right(85)
    t.circle(600*s,40)
    # 绘制另一个绿色叶子
    t.penup()
    t.goto(-150*s,-1000*s)
    t.pendown()
    t.begin_fill()
    t.rt(120)
    t.circle(300*s,115)
    t.left(75)
    t.circle(300*s,100)
    t.end_fill()
    t.penup()
    t.goto(430*s,-1070*s)
    t.pendown()
    t.right(30)
    t.circle(-600*s,35)



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


def main():
    # 初始位置设定
    s = 0.2 # size
    t.setup(450*5*s, 750*5*s)
    t.hideturtle()
    t.title("送小田姐一朵玫瑰花")
    t.pencolor("black")
    t.fillcolor("red")
    t.speed(10)
    t.delay(0)
    t.penup()
    t.goto(0, 900*s)
    t.pendown()
    drawflower(s)
    drawspray(s)
    drawleaves(s)
    colors = ["yellow", "lightblue", "blue", "pink", "seashell"]
    for i in range(20):
        x = random.randint(-200, 200)
        y = random.randint(-350, 350)
        size = random.randint(10, 20)
        color = random.choice(colors)
        t.pu()
        t.goto(x, y)
        t.pd()
        t.color(color)
        t.pensize(size // 4)
        t.speed(0)
        t.delay(0)
        snowflake(size)
        t.seth(random.randint(0, 360))
    t.done()

main()
