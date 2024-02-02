# PythonDraw.py
import turtle

# import引入库
# turtel海龟库


def DrawSanke(r, a, length):
    turtle.seth(-40)
    for i in range(length):
        turtle.circle(r, a)
        turtle.circle(-r, a)
    turtle.circle(r, a / 2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40 * 2 / 3)


turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
DrawSanke(40, 80, 4)
turtle.done()
