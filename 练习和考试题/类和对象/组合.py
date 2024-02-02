class Turtle:
    def tsay(self):
        print('我是一只乌龟')

class Cat:
    def csay(self):
        print('铲屎官的正宫')

class Dog:
    def dsay(self):
        print('人类之友')

class Garden:
    t=Turtle()
    c=Cat()
    d=Dog()
    def say(self):
        self.t.tsay()
        self.c.csay()
        self.d.dsay()

g= Garden()
g.say()