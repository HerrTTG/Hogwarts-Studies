import abc


class Descriptor(abc.ABC):
    def __set_name__(self, owner, name):
        """
        python3。6后支持的描述符方法。让描述符类构造时，不在需要传入属性名。效果等同于__init__。
        """
        self.key_name = name

    def __get__(self, instance, owner):
        # number 和 price，它们的实际值存储在实例的 __dict__ 中
        # instance.__dict__[self.key_name]是储存属性
        return instance.__dict__[self.key_name]

    def __set__(self, instance, value):
        value = self.validata(value)
        instance.__dict__[self.key_name] = value

    @abc.abstractmethod
    def validata(self, value):
        pass


class Quantity(Descriptor):
    def validata(self, value):
        if value > 0:
            return value
        else:
            raise ValueError("must be >0")


class NonBlank(Descriptor):
    def validata(self, value):
        value = value.strip()
        if not value:
            raise ValueError("can not blank")
        return value


class Line():
    """
    托管类
    """
    product: str = NonBlank()  # 描述符实例
    number = Quantity()  # 描述符实例
    price = Quantity()  # 描述符实例

    # 托管属性是由描述符实例管理的类属性。在这里，Line.number 和 Line.price 都是由描述符管理的类属性。
    # 实现__set_name__后描述符实例化构造时不需要传入属性名了

    def __init__(self, product, number, price):
        self.product = product
        self.number = number
        self.price = price

    def subtotal(self):
        return self.number * self.price


def test_1():
    customer = Line("苹果", 10, 0.5)  # 托管实例
    print(customer.subtotal())
    customer.number = -20
