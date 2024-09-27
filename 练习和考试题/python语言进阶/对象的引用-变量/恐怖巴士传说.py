class GhostSchoolBus:
    """
    传闻有这么一个饱受幽灵折磨的校车
    """

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pickup(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return str(self.passengers)


bus1 = GhostSchoolBus()
bus2 = GhostSchoolBus()
bus3 = GhostSchoolBus(["Tom", "Bill"])
bus1.pickup("Dave")
print(bus1)
print(bus2)
print(bus3)


class KillManBus:
    """
    传闻有这么一个上车就会让人消声觅迹的杀人巴士
    """

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pickup(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return str(self.passengers)


# 上车乘客列表
team = ["anne", "Dina", "Pat"]
bus = KillManBus(team)
bus.drop("anne")
print(bus)
print(team)
print(bus.passengers is team)


class GoodBus():
    """
    优秀的宝宝巴士
    """

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 实例属性创建[]副本
        else:
            self.passengers = list(passengers)  # 对形参passengers即实参的别名创建副本，而不是创建一个别名。

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
