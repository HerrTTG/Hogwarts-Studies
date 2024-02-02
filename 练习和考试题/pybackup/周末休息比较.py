# -*- coding: utf-8 -*-
# 一周7天5天进步2天退步
# 按照以上时间模式需要努力多少程度才能与每天进步1%相等呢

dayup = 1.0
dayupp = 0.01


a = (dayup + dayupp) ** 365


def dayUP(x):
    # TODO: write code...
    b = 1.0
    for i in range(365):
        if (i + 1) % 7 in [0, 6]:
            b = b * (1 - 0.01)
        else:
            b = b * (1 + x)
    return b


while dayUP(dayupp) < a:
    dayupp += 0.001
print("工作日的努力参数是:", "{:.3f}".format(dayupp))
