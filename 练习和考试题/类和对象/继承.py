class A:
    x=520
    def hello(self):
        print('你好 我是A')
    def shit(self):
        print('我是你小子没有的')

class B(A):
    x=880
    def hello(self):
        print('你好 我是B')


b=B()
print(b.x)
b.hello()
b.shit() 