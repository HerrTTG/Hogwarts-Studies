# "水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。
s = ""

for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]), 3) + pow(eval(t[1]), 3) + pow(eval(t[2]), 3) == i:
        s += t + ","
print("{}".format(s[:-1]))
