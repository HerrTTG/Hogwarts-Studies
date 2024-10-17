def sub_gen():
    yield 1.1
    yield 1.2


def gen():
    yield 1
    # 调用一个子生成器
    # 传统写法
    # for i in sub_gen():
    #     yield i
    # 3.3后加入
    yield from sub_gen()
    yield 2


for i in gen():
    print(i)
