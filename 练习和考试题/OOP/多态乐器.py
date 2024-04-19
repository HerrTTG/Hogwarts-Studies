# class Violin() 没有继承，但拥有同名方法，一样实现了play函数所需要的功能。
# 说明play这个函数它只关注传入的对象是否拥有实现方法，而不关注类的继承与否。这就是多态

class Instruent():
    def make_sound(self):
        pass


class Erhu(Instruent):
    def make_sound(self):
        print('二胡')

class Pinao(Instruent):
    def make_sound(self):
        print('钢琴')

class Violin():#没有继承父类乐器
    def make_sound(self):
        print('小提琴')


def play(obj):
    obj.make_sound()


if __name__=='__main__':
    er=Erhu()
    pinao=Pinao()
    vilin=Violin()

    play(er)
    play(pinao)
    play(vilin)
