class C:
    def __init__(self,x,y):
        # 当对象被创建后，自动初始化实例的魔法方法。
        # 即，对象创建后无需手动调用，自动就会执行的一个方法。
        # 常被用于各种对象的初始数据实例化。
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y

c=C(2,3)

print(c.add())

print(c.__dict__)