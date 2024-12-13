from typing import Protocol


class StaticProtocol(Protocol):
    """
    类型提示类，类似于ABC，但是不需要显式的继承它。
    """

    def some_method(self) -> None:
        ...

    def another_method(self) -> None:
        ...


class ConcreteClass:
    """
    随意定义的类，没有继承StaticProtocol。而是实现了它描述协议中的所需方法some_method和another_method
    """

    def some_method(self):
        print("Implementing some_method")

    def another_method(self):
        print("Implementing another_method")


# 类型检查工具会确保ConcreteClass符合StaticProtocol
def func(obj: StaticProtocol) -> None:
    """
    定义函数参数时，使用类型标注标注此类型属于静态协议类。并在后调用其方法
    """
    obj.some_method()
    obj.another_method()


# 创建对象并传入函数
obj = ConcreteClass()
# ConcreteClass的实例化对象obj，符合StaticProtocol协议的类所描述的要求。所以类型提示不会出错。
func(obj)


class OtherClass:
    def newmothod(self):
        ...


# obj2是其他不符合条件的类的实例化对象
obj2 = OtherClass()
# 类型提示会提醒
func(obj2)
