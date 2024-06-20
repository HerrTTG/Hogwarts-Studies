# Demo 用于加载不同的文件，对不同的文件作不同的处理
# 问题：如果创建对象的代码比如多，可能还会创建 text ，md，yml 等等
# 简单工厂解决：把对象的创建移动到其它类中， load 方法就会很简洁
from abc import ABCMeta, abstractmethod


class ABCParse(metaclass=ABCMeta):
    # 抽象基类
    # 每个继承的子类都要实现 parse 方法，否则在调用的时候就会报错
    @abstractmethod
    def parse(self):
        pass


# 子类们
class XmlParse(ABCParse):

    def parse(self):
        print("XmlParse")


class JsonParse(ABCParse):

    def parse(self):
        print("JsonParse")


class ExcelParse(ABCParse):

    def parse(self):
        print("ExcelParse")


class CsvParse(ABCParse):

    def parse(self):
        print("CsvParse")


class OtherParse(ABCParse):

    def parse(self):
        print("OtherParse")


class ParseRuleFactory:
    # 简单工厂类：用于实例的创建，根据 rule 创建不同的实例。本质就是把 Demo 中原来创建实例的代码，给迁移过来
    # 可以放在别的包或者模块中
    # 导入工厂。工厂继承此类。

    def create_parse(self, rule):
        # 根据不同的 rule ，创建不同的对象
        if "xml" == rule:

            parse = XmlParse()

        elif "json" == rule:

            parse = JsonParse()

        elif "excel" == rule:

            parse = ExcelParse()

        elif "csv" == rule:

            parse = CsvParse()

        else:

            parse = OtherParse()

        return parse


if __name__ == "__main__":
    class Demo(ParseRuleFactory):
        def load(self, rule):
            # 工厂被初始化时，调用父类的create_parse方法创建实例化，并调用方法
            parse = super().create_parse(rule)
            return parse


    Demo().load("json").parse()
