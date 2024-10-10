class Mydata():
    """
    一个简单的类，定义了两个实例属性xy用于储存xy轴坐标
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 测试代码
a = Mydata(50, 100)
# 无有效的输出，输出结果为<__main__.Mydata object at 0x007C44B0> 因为没有__str__和__repr__
print(a)

b = Mydata(50, 100)

# 无法进行运算
print(a == b)  # 结果为False，因为这个类的__eq__方法只比较对象的id，也就是a和b是不是一个引用。

# 如果想比较或者运算他们的内容，只能对实例对象属性值一个一个提取出来进行
print(a.x == b.x and a.y == b.y)
