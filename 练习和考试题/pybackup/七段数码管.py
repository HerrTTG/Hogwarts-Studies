import turtle as t
import time


def drawline(draw):
    drawgap(5)
    if draw is True:
        # true 落笔 false起飞
        t.pendown()
    else:
        t.penup()
    t.fd(40)
    drawgap(5)
    t.right(90)


def drawDigit(digit):
    if digit in [2, 3, 4, 5, 6, 8, 9]:
        # 根据不同的数字判断是否绘制第一条线
        drawline(True)
    else:
        drawline(False)
    if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        # 根据不同的数字判断是否绘制第二条线
        drawline(True)
    else:
        drawline(False)
    if digit in [0, 2, 3, 5, 6, 8, 9]:
        drawline(True)
    else:
        drawline(False)
    if digit in [0, 2, 6, 8]:
        drawline(True)
    else:
        drawline(False)
    t.left(90)
    # 绘制4次后，返回了起点。调转海龟的方向
    if digit in [0, 4, 5, 6, 8, 9]:
        # 根据不同的数字判断是否绘制第5条线
        drawline(True)
    else:
        drawline(False)
    if digit in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawline(True)
    else:
        drawline(False)
    if digit in [0, 1, 2, 3, 4, 7, 8, 9]:
        # 根据不同的数字判断是否绘制第7条线
        drawline(True)
    else:
        drawline(False)
    t.left(180)


def drawdate(date):
    t.pencolor("red")
    for i in date:
        if i == "-":
            t.write("年", font=("Arial", 18, "normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == "=":
            t.write("月", font=("Arial", 18, "normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == "+":
            t.write("日", font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
            drawgap(15)


def drawgap(x):
    t.penup()
    t.fd(x)


def main():
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    t.speed("fastest")
    t.tracer(False)
    # 绘画速度最快，隐藏绘画过程
    drawdate(time.strftime("%Y-%m=%d+", time.gmtime()))
    t.done()


main()
