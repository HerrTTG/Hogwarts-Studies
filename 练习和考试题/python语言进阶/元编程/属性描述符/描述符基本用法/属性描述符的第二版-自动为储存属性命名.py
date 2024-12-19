class Descriptor():
    """
    描述符类
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
        if value > 0:
            instance.__dict__[self.save_name] = value
        else:
            raise ValueError


class Line():
    """
    托管类
    """
    product: str = ""  # 一般类属性
    number = Descriptor()
    price = Descriptor()

    # 实现__set_name__后,构造描述实例时，不需要传入属性名了

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
    customer.number = -20
