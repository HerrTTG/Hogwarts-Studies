# 问题：如果多个公司都要封装工厂，比如 A, B, C ...公司都要封装自己的工厂，就要封装 n 个工厂类
from abc import abstractmethod, ABCMeta


# 解决：可以使用抽象工厂解决问题，每个工厂类可以创建多个实例，比如 JsonParseRuleFactory ，可以创建 A, B, C 公司的实例

# 一个工厂类，可以生成多个公司的解析方法


class ABCParse(metaclass=ABCMeta):
    # 抽象基类
    # 每个继承的子类都要实现 parse 方法，否则在调用的时候就会报错
    @abstractmethod
    def parse(self):
        pass


class JsonParse(ABCParse):
    def __init__(self, msg="JsonParse"):
        self.msg = msg

    def parse(self):
        print(self.msg)


class IParseRuleFactory(metaclass=ABCMeta):

    @abstractmethod
    def a_create_parse(self):
        pass

    @abstractmethod
    def b_create_parse(self):
        pass

    @abstractmethod
    def c_create_parse(self):
        pass


# 实现时候，一个工厂类就可以生成多个公司的实例
class JsonParseRuleFactory(IParseRuleFactory):

    def a_create_parse(self):
        print("a公司实例被创建")
        """
        省略定制代码 1000行
        """
        return JsonParse("AJsonParse")

    def b_create_parse(self):
        print("b公司实例被创建")
        """
        省略定制代码 1000行
        """
        return JsonParse("BJsonParse")

    def c_create_parse(self):
        """

        """


if __name__ == "__main__":

    # 简单工厂，负责调用复杂工厂去处理复杂的对象生成功过程
    class Demo:
        def load(self, rule):
            if "json" == rule:
                parse = JsonParseRuleFactory()
            else:
                parse = self

            return parse

        def parse(self):
            print("默认公司")


    Demo().load("json").b_create_parse().parse()
