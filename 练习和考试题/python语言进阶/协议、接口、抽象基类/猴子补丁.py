"""
定义一个序列协议类
"""


class Aslist():
    """
    部分实现了序列动态协议，支持索引迭代和in，以及len。但没有其他功能。
    """

    def __init__(self, x):
        self.x = [i for i in x]

    def __getitem__(self, item):
        return self.x[item]

    def __str__(self):
        return str(self.x)

    def __len__(self):
        return len(self.x)


cont = "abcd"

# 可迭代
for i in Aslist(cont):
    print(i)

# 可索引
print(Aslist(cont)[2])

# 可使用in关键字
print("a" in Aslist(cont))

from random import shuffle

# 导入shuffle 尝试打乱序列
# 会报错x[i], x[j] = x[j], x[i]
# TypeError: 'Aslist' object does not support item assignment
# 只是因为shuffle打乱序列，需要对序列中的项做改变，目前此类的实例化属性在实例化后提供变化的接口方法。
# 所以需要实现__setitem__方法
l = Aslist(cont)

try:
    shuffle(l)
except TypeError as e:
    print(e)
else:
    print(l)


# 打补丁
def setvalue(object: Aslist, postion, value):
    # 定义一个补丁函数
    # 参数相当于 self,postion,value
    object.x[postion] = value


# 给类打上补丁
Aslist.__setitem__ = setvalue
shuffle(l)
print(l)
