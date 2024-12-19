import abc

class Descriptor(abc.ABC):
    """
    描述符的抽象基类，
    实现设置读值和自动命名。
    且新增一个抽象的校验方法。
    在设值时，调用它进行检查
    """

    def __set_name__(self, owner, attr_name):
        """
        python3。6后支持的描述符方法。让描述符类构造时，不在需要传入属性名。效果等同于__init__。
        """
        self.save_name = f"__{attr_name}"

    def __get__(self, instance, owner):
        # number 和 price，它们的实际值存储在实例的 __dict__ 中
        # instance.__dict__[self.key_name]是储存属性
        return instance.__dict__[self.save_name]

    def __set__(self, instance, value):
        instance.__dict__[self.save_name] = self.validata(value)


    @abc.abstractmethod
    def validata(self, value):
        """
        抽象方法，要求子类必须实现
        """
        pass


class Quantity(Descriptor):
    """
    继承描述符类的子类。
    根据需求实现不同的校验方法
    """
    def validata(self, value):
        if value > 0:
            return value
        else:
            raise ValueError("must be >0")


class NonBlank(Descriptor):
    """
    继承描述符类的子类。
    根据需求实现不同的校验方法
    """
    def validata(self, value):
        value = value.strip()
        if not value:
            raise ValueError("can not blank")
        return value


class Line():
    """
    托管类
    """
    product: str = NonBlank()  # 字符串类型的属性托管给NonBlank描述符子类，来限制该属性不能为空字符串
    number = Quantity()  # number和price属性托管给Quantity来限制不能小于0
    price = Quantity()


    def __init__(self, product, number, price):
        self.product = product
        self.number = number
        self.price = price

    def subtotal(self):
        return self.number * self.price


# 测试代码
if __name__ == "__main__":
    customer = Line("苹果", 10, 0.5)  # csutomer是托管类生成的托管实例
    print(customer.subtotal())
    # customer.number = -20
    customer.product=""
