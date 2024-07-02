from abc import ABCMeta
from abc import abstractmethod


class Subject(metaclass=ABCMeta):
    # 主要用于定义代理和真实实现类的共同接口
    # 使用抽象基类的设计方法，限制代理类和真实实现类。
    # 让代理类和真实实现类必须拥有某些共同的方法。
    # 以便任何需要使用真实实现的地方都可以用Proxy完成。

    def __init__(self):
        print("接口定义代理和realsubject，必须都实现同一个方法")

    @abstractmethod
    def givegift(self, name):
        pass
