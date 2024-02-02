class C:
    def __init__(self):
        self.__x=250
    @property
    def x(self):
        return self.__x

    #setter是赋值的拦截。用装饰器的方法来是下面的方法拥有拦截的能力
    @x.setter
    def x(self,vaule):
        self.__x=vaule

    # deleter 是del的拦截。用装饰器的方法来是下面的方法拥有拦截的能力
    @x.deleter
    def x(self):
        del self.__x

c=C()
print(c.x)
c.x=150
print(c.x)
print(c.__dict__)
del c.x
print(c.__dict__)