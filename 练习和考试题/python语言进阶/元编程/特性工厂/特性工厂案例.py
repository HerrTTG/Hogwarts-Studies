def factory(prop_name):
    """
    特性的生产工厂，一个闭包函数。
    {prop_name}为特性和客户侧暴露的实例化对象名称。
    内部储存实例化属性为_{prop_name}

    实现get和set方法。
    最后返回一个特性对象。

    """

    def _get_prop(instance):
        return instance.__dict__[f"_{prop_name}"]

    def _set_prop(instance, value):
        """
        这里选择直接更新实例化属性字典dict来赋值实例化属性，
        是为了防止直接赋值实例化属性发生不必要的bug。
        instance.prop_name 是给对象赋予"prop_name"这个属性，而不是self.{prop_name}
        """

        if value > 0:
            instance.__dict__[f"_{prop_name}"] = value
        else:
            raise ValueError("vaule must gt 0")

    return property(_get_prop, _set_prop)


class Line():
    price: int | float = factory("price")
    number: int | float = factory("number")

    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number

    def subtotal(self):
        return self.price * self.number


customer1 = Line("苹果", 10, 20)
print(vars(customer1))

customer1.number = -20
print(customer1.subtotal())
