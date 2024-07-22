# 多态是指同一个运算符、函数、对象在不同的场景下具有不同的作用效果这个技能


class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass

class Squre(Shape):
    def __init__(self,length):
        super().__init__('正方形')
        self.length=length
    def area(self):
        return self.length * self.length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('圆心')
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


class Triangle(Shape):
    def __init__(self, base,heigh):
        super().__init__('三角形')
        self.base = base
        self.heigh = heigh

    def area(self):
        return self.base*self.heigh /2

s=Squre(5)
c=Circle(6)
t=Triangle(3,4)

def areacal(x):
    # areacal 这个函数就具有多态性了，该函数接受不同的对象作为参数，在不检查其类型的情况下去执行对象所拥有的方法
    # 他只关心参数x是否能做到area方法，x本身是什么并不关心
    return x.area()

print(areacal(s))
