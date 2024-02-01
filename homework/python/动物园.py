'''
作业要求
设计一个简单的动物园系统，其中包含不同类型的动物（如狗、猫和鸟）。
每个动物都有自己的属性（如名字、年龄）和行为（如发出声音）。使用封装、继承和多态来完成。
'''


class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print(f'我是{self.name}，我今年{self.age}岁了')
    def singe(self):
        print('唱歌')

class Cat(Animal):
    def singe(self):
        print('喵喵喵~')

class Dog(Animal):
    def singe(self):
        print('旺旺旺！')


def zoo(x:object):
    x.say()
    x.singe()



if __name__=='__main__':
    zoo(Cat('美短猫','2'))
    zoo(Dog('柴柴','5'))

