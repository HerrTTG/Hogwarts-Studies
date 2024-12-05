class GoodBus():
    """
    优秀的宝宝巴士
    """

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 实例属性创建[]副本
        else:
            self.passengers = list(passengers)  # 对形参passengers即实参的别名创建副本，而不是创建一个别名。
            # 但这里要注意 self.passengers=list(passengers) 只是浅拷贝，如果passengers 容器内包含可变容器，则要使用深拷贝
            # self.passengers=copy.deepcopy(passengers)

    def pickup(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return str(self.passengers)


team = ["anne", "Dina", "Pat"]
baobaobus1 = GoodBus()
baobaobus2 = GoodBus()
baobaobus3 = GoodBus(team)

baobaobus1.pickup("Bill")
print(baobaobus1)
print(baobaobus2)
print(baobaobus3)
baobaobus3.drop("anne")
print(baobaobus3)
print(team)
