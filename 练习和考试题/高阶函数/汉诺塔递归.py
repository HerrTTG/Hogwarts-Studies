count = 0


def hanoi(n, src, dst, mid):
    # n圆盘的数量 src初始柱子 dst目标柱子 mid中间柱子
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


hanoi(3, "A", "C", "B")
print(count)
