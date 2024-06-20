# Demo 用于加载不同的文件，对不同的文件作不同的处理
from abc import ABCMeta
from abc import abstractmethod


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

    def other(self):
        pass


class ExcelParse(ABCParse):

    def parse(self):
        print("ExcelParse")


class CsvParse(ABCParse):

    def parse(self):
        print("CsvParse")


class OtherParse(ABCParse):

    def parse(self):
        print("OtherParse")


if __name__ == "__main__":

    # 工厂
    class Demo:

        def __init__(self, rule):
            # 根据条件不同生成不同的实例化
            # 根据不同的 rule ，创建不同的对象

            parse: object = None

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

            # 调用对象的方法进行操作
            parse.parse()


    # 相当于接口，用于规范各个解析类

    ob1 = Demo("json")
    ob2 = Demo("csv")
