class C:
    def __init__(self):
        self.__x=250

    # 属性化一个方法，当对象调用.x的时候等于执行此函数。
    # 语法相当于 x=property(x)
    # 函数用于返回一个property属性对象
    # 表明x不是一个变量也不是一个可用直接调用的方法。即只读
    @property
    def x(self):
        return self.__x

    # setter是赋值的拦截。用装饰器的让下面的方法拥有拦截的能力
    #即当对象对x进行赋值时，执行此方法
    @x.setter
    def x(self,vaule):
        self.__x=vaule

    # deleter 是del的拦截。用装饰器来让下面的方法拥有拦截的能力
    # 即当对象对x进行删除时，执行此方法
    @x.deleter
    def x(self):
        del self.__x

c=C()
print(c.x)
print(c.__dict__)

c.x=150
print(c.x)
print(c.__dict__)

del c.x
print(c.__dict__)