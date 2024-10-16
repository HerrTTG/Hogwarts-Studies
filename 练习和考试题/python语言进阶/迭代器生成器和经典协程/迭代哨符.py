from random import randint


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)  # 哨符为1
print(d6_iter)
for i in d6_iter:
    # 一直循环
    # 直到迭代器生成出哨符值抛出异常停止
    print(i)
