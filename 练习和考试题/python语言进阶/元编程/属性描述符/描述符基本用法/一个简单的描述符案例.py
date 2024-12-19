class Descriptor():
    """
    描述符类
    """

    def __init__(self, attr_name):
        # 将托管属性名，和存储属性名拼接绑定
        self.save_key_name = f"__{attr_name}"

    def __get__(self, instance, owner):
        # number 和 price，它们的实际值存储在实例的 __dict__ 中
        # instance.__dict__[self.key_name]是储存属性
        return instance.__dict__[self.save_key_name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.save_key_name] = value
        else:
            raise ValueError


class Line():
    """
    托管类
    """
    product: str = ""  # 一般类属性
    number = Descriptor("number")  # Descriptor("number") 构造的对象就是描述符实例
    price = Descriptor("price")
    # 托管属性是由描述符实例管理的类属性。在这里，Line.number 和 Line.price 都是由描述符管理的类属性。
    # 所以number和price是托管属性

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
