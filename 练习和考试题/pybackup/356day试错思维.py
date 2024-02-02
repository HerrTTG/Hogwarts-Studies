# 一周7天5天进步2天退步
# 按照以上时间模式需要努力多少程度才能与每天进步1%相等呢

day = 1.0
dayq = 0.01
dayd = 1.0


daya = pow(day + dayq, 365)

# 计算思维
for i in range(365):
    if (i + 1) % 7 in [0, 6]:
        dayd = dayd * (1 - dayq)
    else:
        dayd = dayd * (1 + dayq)

差值 = daya - dayd

print(daya, dayd, 差值, "在根据差值计算需要提升多少努力百分比，计算思维很麻烦")


# 试错思维
def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if (i + 1) % 7 in [0, 6]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup


dayt = 0.01
while dayUP(dayt) < daya:
    dayt += 0.001
print(dayt, "试错思维就是将计算设置为一个函数,求解值配置为一个变量。通过while循环来循环求解变量值")
