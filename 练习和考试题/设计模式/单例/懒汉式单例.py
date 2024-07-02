from threading import Lock


class IdMaker:
    # 饿汉单例就是拦截类被实例化的过程，直接拒绝生成新的实例
    # 而是定义一个方法，根据类属性来判断是否需要生成新的势实例。并且进行上锁。

    # 饿汉像一个饥饿的人，在菜被端上来前就进行拦截。并只准许自己吃。
    # 代价就是初始化的过程可能很耗时间，无异议的动作可能也很多。拦截了但可能并不需要。

    # 懒汉则是根据判断来确实是否需要实例化上桌吃饭，需要的话也是独自一人霸占，不准许更多实例。

    # 申请一个线程锁
    __instance_lock = Lock()

    # 定义一个类变量用来记录对象，初始默认值赋予None
    __instance = None

    # __id 也是类变量，多个实例或类共享
    # 测试目标
    __id = -1

    def __new__(cls):
        #利用new魔法，在类创建对象前进行拦截。
        # 阻止类被实例化
        raise ImportError("Instantition not allowed")

    # 类方法不用实例化也能调用，因为我们不允许直接进行实例化，所以要暴漏类方法来判断是否创建实例。
    # 主动写一个获取实例化的方法
    # 格外注意的是__new__方法实例化不会出现多线程并行。这是python做的特殊处理。
    # 而自己写的方法或函数，是可能会出现并行的。
    # 为了实现单例，最好加上锁。来确保创建实例的方法是单线程执行的。
    # 确保哪怕get_instance方法被并行执行，也会被锁住。等待第一次运行完后释放结果。
    # 那么第二次在执行get_instance方法，就会因为__instance不为None而跳过生成新的实例实现单例。
    @classmethod
    def get_instance(cls):

        # with 会帮我们自动的上锁和释放，不用我们操心
        with cls.__instance_lock:
            if cls.__instance is None:
                # 为None说明类还没被实例化，调用父类的 __new__ ，参数接收一个类名，会返回类的实例化对象
                # 将对象值赋予类属性cls.__instance后返回
                cls.__instance = super().__new__(cls)

        return cls.__instance

    def get_id(self):
        # 计数器，在获取前，进行 + 1 后返回值
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
