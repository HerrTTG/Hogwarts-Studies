import math


# 本案可以巧妙的利用数据模型中的容器API的子类，
# 来将一个二维向量元组，模拟成可运算的数值类型。


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # repr用于获取对象的字符串表示形式
        # 如果没有则print打印Vector的对象，控制台会显示为Vector object at 0x01A41CB0
        # !r表示以标准形式显示属性，使其不会变为Vector('1','2')
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # 只要实现了bool方法或者len，就可以对if assert 等判断进行定制。
    # python在判断对象的真假时，默认先判断bool来试图得到一个true或者false。
    # 如果对象没有bool，则试图调用len。来判断对象值是否大于0。
    def __bool__(self):
        return bool(self.x or self.y)
        # return bool(abs(self))

    # 只要实现了加法，那么就可以用+号，或者add函数
    def __add__(self, other):
        # 这里other是指另外一个类对象，v1+v2,即v1对应self,v2对应+号后面的v2
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 只要实现了mul，就能使用*
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


a = Vector(1, 2)
b = Vector(2, 1)
print(a)
print(a + b)
print(bool(a + b))
print(a * 0)
print(bool(a * 0))
