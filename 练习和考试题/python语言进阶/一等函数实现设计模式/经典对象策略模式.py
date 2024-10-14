from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    """
    客户对象的数据模型类,使用具名元组进行定义。
    分别是
    name:客户名称
    points:客户的积分
    """
    name: str
    points: int


class LineItem(NamedTuple):
    """
    客户购买的商品的数据模型类,使用具名元组进行定义。
    product:商品名称
    quantity:购买商品数量
    price:单价
    """
    product: str
    quantity: int
    price: Decimal

    def Itemtotal(self):
        return self.price * self.quantity


class Order(NamedTuple):
    """
    上下文数据模型类，使用具名元组进行定义。
    customer:客户实例属性，指向Customer类的实例化对象
    catr:客户的购物车实例属性，指向一个序列，里面的项由客户购买的商品类LineItem的实例化对象们组成
    policy:客户所对应的折扣方法，可为空且默认为空。指向Policy类的实例化对象。
    """
    customer: Customer
    cart: Sequence[LineItem]
    policy: Optional['Policy'] = None

    def totla(self):
        """
        获取客户的总购物消费值
        """
        totals = (item.Itemtotal() for item in self.cart)  # 从客户的购物车实例属性序列中取出每一个项，调用项的Itemtotal方法
        return sum(totals, start=Decimal(0))  # 为什么这么写

    def due(self):
        if self.policy is None:
            discount = Decimal(0)
        else:
            discount = self.policy.discount(self)  # 如果有对应的策略，则将Order自身的实例化对象传入。
        return self.totla() - discount

    def __str__(self):
        return f"<Order total:{self.totla():.2f} due:{self.due():.2f}>"


class Policy(ABC):
    """
    策略的共同接口,继承的子策略必须实现折扣计算这个方法
    """

    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        pass


class PointsPolicy(Policy):
    def discount(self, order: Order) -> Decimal:
        """
        积分折扣策略，返回折扣额度
        """
        rate = Decimal('0.05')  # 定义折扣率为0.05
        if order.customer.points >= 1000:
            # 判断客户的积分是否大于等于1000
            return order.totla() * rate  # 返回购物车总金额*折扣率的折扣额度
        return Decimal(0)


class ItemPolicy(Policy):
    def discount(self, order: Order) -> Decimal:
        """
        商品数量折扣策略，返回折扣额度
        """
        discount = Decimal(0)
        for item in order.cart:  # 循环从购物车中获取每一个Item的订单。
            if item.quantity >= 20:  # 如果数量大于20
                discount += item.Itemtotal() * Decimal('0.1')  # 则该商品的总额进行折扣额计算，返回折扣额度
        return discount


class CartPolicy(Policy):
    def discount(self, order: Order) -> Decimal:
        """
        购物车折扣策略，返回折扣额度
        """
        rate = Decimal('0.07')
        distinct_item = {item.product for item in order.cart}  # 从购物车中循环取出Item，将Item的商品名称构造入集合
        # 利用集合中项不重复的特性排重
        if len(distinct_item) >= 10:  # 如果不同商品数大于10
            return order.totla() * rate  # 返回购物车总金额*折扣率的折扣额度
        return Decimal(0)


if __name__ == "__main__":
    """测试代码"""
    xueqin = Customer("xueqin", 0)
    cart = (LineItem("banana", 4, Decimal('.5')),
            LineItem("Apple", 20, Decimal('1.5')),
            LineItem("watermelon", 5, Decimal(5)))

    print(Order(xueqin, cart=cart, policy=ItemPolicy()))

    haizhenyu = Customer("haizhenyu", 1000)
    print(Order(haizhenyu, cart=cart, policy=PointsPolicy()))
