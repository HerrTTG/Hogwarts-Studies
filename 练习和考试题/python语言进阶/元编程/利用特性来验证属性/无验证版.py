# 客户可以对实例属性做修改，但没有如果没有验证数据的正确性，则可能引发bug

class Lineitem():
    def __init__(self, product, price, number):
        self.product = product
        self.price = price
        if number > 0:
            self.number = number
        else:
            raise ValueError

    def subtotal(self):
        return self.price * self.number


customer1 = Lineitem("苹果", 0.5, 20)
customer1.number = -20

# 如此案例中，在实例化构造时会验证属性的正确性。判断number是否>0
# 但是实例化后，用户可以使用对实例属性赋值的方法重新赋值，并绕过构造方法中的正确性验证。
# 实例属性number 被成功改为-20

print(customer1.subtotal())
