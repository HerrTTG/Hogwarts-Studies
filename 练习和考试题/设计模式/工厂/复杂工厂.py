# 问题：简单工厂不能解决创建实例的代码可能很复杂，即使迁移到了简单工厂中，复杂的创建过程依旧存在
import random

from abc import ABCMeta, abstractmethod


# 目标实例化的类模组
class ABCParse(metaclass=ABCMeta):
    # 抽象基类
    # 每个继承的子类都要实现 parse 方法，否则在调用的时候就会报错
    @abstractmethod
    def parse(self):
        pass


class XmlParse(ABCParse):
    def __init__(self, msg="XmlParse"):
        self.msg = msg

    def parse(self):
        print(self.msg)


class JsonParse(ABCParse):

    def __init__(self, msg="JsonParse"):
        self.msg = msg

    def parse(self):
        print(self.msg)


# 复杂工厂，负责生成实例化对象
class ABCFactory(metaclass=ABCMeta):
    # 抽象基类
    # 每个继承的子类都要实现 create_parse 方法，否则在调用的时候就会报错
    @abstractmethod
    def create_parse(self):
        pass


class JsonParseRuleFactory(ABCFactory):

    def create_parse(self) -> object:
        # 省略 复杂的1000 行代码
        # 对实例化做一定的处理
        # 最终返回一个实例化对象
        msg = str(random.Random().randint(0, 1000)) + "JsonParse"
        return JsonParse(msg)


class XmlParseRuleFactory(ABCFactory):
    def create_parse(self) -> object:
        # 省略 复杂的1000 行代码
        # 最终返回一个实例化对象

        msg = str(random.Random().randint(0, 1000)) + "JsonParse"
        return XmlParse(msg)


if __name__ == "__main__":

    # 简单工厂，负责调用复杂工厂去处理复杂的对象生成功过程
    class Demo:
        def load(self, rule):
            if "xml" == rule:
                parse = XmlParseRuleFactory().create_parse()

            elif "json" == rule:
                parse = JsonParseRuleFactory().create_parse()
            else:
                parse = self

            return parse

        def parse(self):
            print("简单工厂")


    Demo().load("json").parse()
