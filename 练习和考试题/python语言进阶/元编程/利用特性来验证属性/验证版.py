# 客户可以对实例属性做修改，但没有如果没有验证数据的正确性，则可能引发bug
# 所以利用特性来保护实例化属性，并且做相关的验证

class Lineitem():
    __number: int | float  # 被保护的真正实例化属性

    def __init__(self, product, price, number):
        self.product = product
        self.price = price
        self.number = number  #     # self.number = number已经不是对实例属性操作了，而是在调用设值方法

    def subtotal(self):
        return self.price * self.number

    # 众所周知装饰器在引入的时候执行，执行后self.number就等于number方法了
    @property
    def number(self):
        """特性的读值方法"""
        #返回被保护的私有实例化属性
        return self.__number

    #
    @number.setter  # 把读值和设值方法绑定在一起。
    def number(self, number):
        """特性的设值方法"""
        if number > 0:
            #对验证要求的值，才对被保护的私有实例化属性赋值
            self.__number = number
        else:
            raise ValueError


def test():
    customer = Lineitem("苹果", 0.5, -10)
    customer.subtotal()


def test1():
    customer = Lineitem("苹果", 0.5, 10)
    customer.number = -10
    customer.subtotal()


def test2():
    customer = Lineitem("苹果", 0.5, 10)
    customer.number = 20
    customer.subtotal()
