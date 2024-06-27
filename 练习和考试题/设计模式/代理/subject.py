from abc import ABCMeta
from abc import abstractmethod


class Subject(metaclass=ABCMeta):

    def __init__(self):
        print("接口定义代理和realsubject 必须都实现同一个方法")

    @abstractmethod
    def givegift(self, name):
        pass
