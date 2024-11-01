def func():
    num = 1000

    def inner(value):
        nonlocal num
        num += value
        return num

    return inner


t = [func()(i * 10) for i in range(1, 4)]
print(t)
