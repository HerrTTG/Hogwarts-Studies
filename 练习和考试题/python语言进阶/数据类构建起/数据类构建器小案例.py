import dataclasses


class Mydata():
    """
    一个简单的类，定义了两个实例属性xy用于储存xy轴坐标
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 测试代码
a = Mydata(50, 100)
# 无有效的输出
print(a)
b = Mydata(50, 100)
# 结果为False，因为这个类的__eq__方法只比较对象的id  a和b是不同的实例对象，所以为False
print(a == b)
# 相比较他们的内容是否一致，只能一个一个实例对象比较
print(a.x == b.x and a.y == b.y)

# 数据类构造器
from collections import namedtuple

# namedtuple 是一个工厂方法，可定义指定的名称和字段来构建一个tuple类的子类

# 工厂方法返回一个新的子类Mydata2
Mydata2 = namedtuple("Mydata2", ['x', 'y'])

# 并且继承自tuple
print(issubclass(Mydata2, tuple))

# 传入实例属性构造对象c
c = Mydata2(50, 100)
# 输出结果类似tuple清晰可见Mydata2(x=50, y=100)
# 有用的__repr__
print(c)

# 可进行简单快捷数据比对
# 有意义的__eq__
print(c == Mydata2(x=50, y=100))

import typing

Mydata3 = typing.NamedTuple("Mydate3", [('x', int), ('y', int)])
d = Mydata3(50, 100)
print(d)
print(typing.get_type_hints(d))


class Mydata4(typing.NamedTuple):
    x: int
    y: int

    # 定义str方法来展示
    def __str__(self):
        return f"(x={self.x},y={self.y})"


e = Mydata4(50, 100)
print(e)
print(issubclass(Mydata4, tuple))

from dataclasses import dataclass


@dataclass(frozen=True)
class Mydata5:
    x: int
    y: int

    # 定义str方法来展示
    def __str__(self):
        return f"(x={self.x},y={self.y})"


f = Mydata5(50, 100)
print(f)
print(issubclass(Mydata5, tuple))

print(e._asdict())
print(dataclasses.asdict(f))

print(Mydata4._fields)
print(dataclasses.fields(Mydata5))
print(typing.get_type_hints(f))

dataclasses.replace(f, x=100)
print(f)
