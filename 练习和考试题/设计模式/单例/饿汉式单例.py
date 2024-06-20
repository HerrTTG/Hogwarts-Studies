class IdMaker:
    # python 的类变量会被多个类，实例共享

    __instance = None

    # __id 也是类变量，多个实例或类共享

    __id = -1

    def __new__(cls):
        # python 在类加载阶段，通过父类的 __new__ 创建实例，如果我们重写 __new__
        # 就不会调用父类的 __new__ ，就会调用我们写的 __new__ 创建实例
        # __new__ 需要返回一个实例，如果不返回，就不会实例化

        # 判断类属性__instance是否为None，不为None说明类已经被实例化，返回上一次实例化的结果(保证单例)
        if cls.__instance is None:
            # 为None说明类还没被实例化，调用父类的 __new__ ，参数接收一个类名，会返回类的实例化
            # 将值赋予类属性cls.__instance后返回
            cls.__instance = super().__new__(cls)

        return cls.__instance

    # 计数器，在获取前，进行 + 1

    def get_id(self):
        self.__id += 1

        return self.__id

    @classmethod
    def changeid(cls, value):
        cls.__id = value


def id_maker():
    id1 = IdMaker().get_id()

    id2 = IdMaker().get_id()

    id3 = IdMaker().get_id()

    print(id1, id2, id3)


if __name__ == "__main__":
    id_maker()
    # 0 1 2
    IdMaker.changeid(10)
    id_maker()
    # 3 4 5

    # 从结果来看 每一个对象id1、id2、id3实际上指向的都是同一个实例。
    # 并且在类修改了自己的类属性后，再次执行也不会新建实例，所以计算结果还是按旧实例的__id值为准。

    # 饿汉单例就是拦截类被实例化的过程，定义一个类变量来共享和判断实例是否存在。
    # 存在就返回此实例而不新建
