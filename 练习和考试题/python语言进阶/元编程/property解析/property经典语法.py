class Lineitem():
    def __init__(self, product, price, number):
        self.product = product
        self.price = price
        self.number = number

    def subtotal(self):
        return self.price * self.number

    def func1(self):
        return self.__number

    def func2(self, vaule):
        if vaule > 0:
            self.__number = vaule
        else:
            raise ValueError

    number = property(func1, func2)


customer = Lineitem("苹果", 0.5, 10)
customer.number = 20
print(customer.subtotal())
