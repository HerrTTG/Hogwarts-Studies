# 单例是解决多线程处理共享资源的最好设计模式。
# 如 需要对某个测试目标__id 进行多线程累加。
# 如果不使用单例的方式，多个线程分别实例化自己的对象进行处理，结果只是在自身对象身上进行累加。
# 而单例实际是对同一个对象进行操作。



class IdMaker:
    # 饿汉单例就是拦截类被实例化的过程，定义一个类变量来共享和判断实例是否存在。
    # 存在就返回此实例而不新建

    __instance = None

    # __id 也是类变量，多个实例或类共享
    # 测试目标
    __id = -1

    def __new__(cls):
        #利用new魔法，在类创建对象前进行拦截，判断类属性是否为空
        if cls.__instance is None:
            # 为None说明类还没被实例化，调用父类的 __new__ ，参数接收一个类名，会返回类的实例化对象
            # 将对象值赋予类属性cls.__instance后返回
            cls.__instance = super().__new__(cls)

        # 此时类属性值已经从None变为对象值，不在为空。下一次类试图创建新对象的时候都会直接返回寄存在类属性中的原本的对象值
        return cls.__instance


    def get_id(self):
        # 计数器，在获取前，进行 + 1 后返回值
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
    # 每次调用get_id都是同一个实例化对象。所以返回结果是累加的。
    # 0 1 2

    # 修改类属性值后
    IdMaker.changeid(10)
    id_maker()
    # 还是累加获取
    # 3 4 5

    # 从结果来看 每一个对象id1、id2、id3实际上指向的都是同一个实例。
    # 并且在类修改了自己的类属性后，再次执行也不会新建实例，所以计算结果还是按旧实例的__id值为准。
