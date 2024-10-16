s = 'ABC'  # 可迭代对象
t = iter(s)  # 调用iter传入可迭代对象，获取迭代器对象
print(t)  # str_ascii_iterator
print(dir(t))
while True:
    try:
        print(next(t))  # 不断在迭代器上调用next函数，获取下一项
    except StopIteration:  # 直到没有剩余项时，抛出异常
        del t  # 释放t引用，废弃迭代器对象
        break  # 跳出循环

# 等价于下面的循环
for i in s:
    print(i)
