import turtle as t

t.setup(600, 600)


for a in range(4):
    t.seth(a * 90 + 45)
    t.fd(150 * 8 / (2 * 3.1415))
    # 根据圆周得出半径，并且画出半径长度的直线
    t.left(90)
    t.circle(150 * 8 / (2 * 3.1415), 45)
    t.goto(0, 0)
