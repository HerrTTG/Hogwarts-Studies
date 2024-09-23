# 如for循环其实调用的iter(x) 而iter(x) 调用的又是x.__iter__()将x这个可迭代对象转化为迭代器，再通过__next__一个一个迭代结果
# 或者利用x.__getitem__()逐个获取可迭代对象的返回值
x = [1, 2, 3]
for i in x:
    print(i)

# 方法一:转为迭代器
a = iter(x)
# a=x.__iter__()
print(type(a), dir(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())

# 方法二:或者直接调用序列的getitem
print(x.__getitem__(0))
print(x.__getitem__(1))
print(x.__getitem__(2))
