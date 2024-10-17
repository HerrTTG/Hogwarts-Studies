from collections.abc import Generator


def avg() -> Generator[float, float, None]:
    # Generator[float,float,None]表示生成器将返回float类型的项，同时也接受.send()函数传入的float类型的值
    total = 0.0
    count = 0
    avg = 0.0
    while True:
        _tmp = yield avg  # 先提供一个项出去，send()方法接收到值后，赋值给_tmp
        total += _tmp
        count += 1
        avg = total / count


avg = avg()
next(avg)  # 启动协程
# avg.send(None) 这么写也能启动写成
print(avg.send(10))
print(avg.send(12))
