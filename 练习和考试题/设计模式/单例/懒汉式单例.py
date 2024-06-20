from threading import Lock


class IdMaker:
    # 申请一个线程锁

    __instance_lock = Lock()

    # python 的类变量会被多个类，实例共享

    __instance = None

    # __id 也是类变量，多个实例或类共享

    __id = -1

    def __new__(cls):
        # 如果 __new__ 抛出异常，就不允许调用者进行实例化
        # 阻止类被实例化
        raise ImportError("Instantition not allowed")

    # 类方法不用实例化也能调用，因为我们不允许进行实例化，所以要使用类方法。
    @classmethod
    def get_instance(cls):
        # 主动写一个获取实例化的方法
        # __new__方法实例化不会出现多线程并行
        # 但自己写的方法来做实例化，可能会出现
        # 最好手动添加互斥锁。
        # with 会帮我们自动的上锁和释放，不用我们操心
        # 确保哪怕get_instance方法被并行执行，也会被锁住。等待第一次运行完后释放结果。
        # 那么第二次就会因为__instance不为None而跳过生成新的实例实现单例。
        with cls.__instance_lock:
            if cls.__instance is None:
                # 因为我们的 __new__ 代码不允许进行实例化，所以可以借用父类的 __new__ 进行实例化

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
    # IdMaker 是单例类，只允许有一个实例
    # IdMaker.get_instance() 才获取或者新建了一个实例。才可以调用get_id()

    id1 = IdMaker.get_instance().get_id()

    id2 = IdMaker.get_instance().get_id()

    id3 = IdMaker.get_instance().get_id()

    print(id1, id2, id3)


if __name__ == "__main__":
    id_maker()
    # 0 1 2
    IdMaker.changeid(99)
    id_maker()
    # 3 4 5

    # 饿汉单例就是拦截类被实例化的过程，直接拒绝生成新的实例
    # 而是定义一个方法，根据类属性来判断是否需要生成新的势实例。并且进行上锁。
