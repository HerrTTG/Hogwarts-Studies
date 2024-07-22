# 一个类继承多个父类的访问顺序一定是由左向右的。
# 如果AB中存在相同的属性和方法，c如果自身没有这些属性和方法。那么优先调用A类中的
# 只有当自身找不到，并且A中没有，才会去找B的属性和方法来解决问题

class A:
    x=520
    def hello(self):
        print('你好 我是A')
    def shit(self):
        print('我是你小子没有的')

class B:
    x=880
    y=123
    def hello(self):
        print('你好 我是B')

class C(A,B):
    pass

c=C()
print(c.x)
print(c.y)
c.hello()
c.shit()