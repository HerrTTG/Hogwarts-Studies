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
    return x.area()

print(areacal(s))

#areacal 这个函数就具有多态性了，该函数接受不同的对象作为参数，在不检查其类型的情况下去执行对象所拥有的方法
