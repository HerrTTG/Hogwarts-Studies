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
