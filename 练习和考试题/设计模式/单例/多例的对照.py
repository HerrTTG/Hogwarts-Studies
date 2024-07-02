class IdMaker:
    __id = -1

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
    # 0 0 0
    IdMaker.changeid(2)
    id_maker()
    # 3 3 3

# 可以从对照结果来看，多实例实际上每个对象都是独立继承的（类所拥有的所有方法和属性值）

# 一开始对象id1、id2、id3拥有的属性值__id都是-1
# getid方法得到的结果都是0
# 修改类属性值后，再次调用getid方法
# 得到的结果都是3
