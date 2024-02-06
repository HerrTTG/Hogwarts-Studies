# 核心思想是当抛洒的点足够多，就近似约等于所有点覆盖了所有的面积。进而可以得到面积，在ton过面积比来计算圆周率。
from random import *
from time import *

DARTS = pow(2,int(input()))
# DARTS = 2**x方
# 设抛洒点的数量 2的20次方覆盖1为单位正方形
hits = 0.0
# 击中靶心的数量，这里是代表抛洒点进入圆内的数量
start = perf_counter()
seed(123)
for i in range(1, DARTS + 1):
    x, y = random(), random()
    #以1为半径的原计算，根据需要时可以变动的。比如5为单位，那么随机就取1,5的浮点数。同时距离圆心距离也是小于5即可
    dist = pow(x**2 + y**2, 0.5)
    # 计算点到圆心的距离
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
# 圆周率等于击中靶心的数量处于总抛洒数，即4分之一个圆的面积/正方形的面积。乘4
print("{:.6f}".format(pi))
# print("计算时间:{:.5f}s".format(perf_counter() - start))
