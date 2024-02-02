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