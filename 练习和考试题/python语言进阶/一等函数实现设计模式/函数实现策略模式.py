"""
假如有个电商网站，制订了以下折扣规则：
1.有1000或者以上积分的客户，每个订单享受5%折扣。
2.同一订单中，单个商品的数量达到20个或以上，享10%折扣。
3.订单中不同商品的数量达到10个或者以上，享7%折扣。

函数式实现策略折扣实，实现了自动使用最佳折扣方案，但未实现自动注册
"""


from collections.abc import Sequence
from decimal import Decimal
from functools import lru_cache
from typing import NamedTuple, Optional, Callable


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

    @property
    @lru_cache
    def itemtotal(self):
        """
          计算购买的Item总价格
        """
        return self.price * self.quantity


class Order(NamedTuple):
    """
    上下文数据模型类，使用具名元组进行定义。
    customer:客户实例属性，指向Customer类的实例化对象
    catr:客户的购物车实例属性，指向一个序列，里面的项由客户购买的商品类LineItem的实例化对象们组成
    policy:客户所对应的折扣方法，可为空且默认为空。指向一个可调用对象(函数)且此函数支持传入Order对象作为参数，返回Decimal
    """
    customer: Customer
    cart: Sequence[LineItem]
    # 这句话的意思是，policy是一个可选项，其可能是一个Callable，并且能被传递一个Order类型参数，返回一个Decimal类型。
    # 在这里，暗指折扣策略的函数们。
    policy: Optional[Callable[['Order'], Decimal]] = None

    @property
    @lru_cache()
    def totla(self):
        """
        获取客户的总购物消费值
        """
        # 生成器推导式负责迭代，取出每一个商品类对象，获取itemtotal的值
        # 从零开始累加
        return sum((item.itemtotal for item in self.cart), start=Decimal(0))  #

    def due(self):
        """
        处理客户订单的优惠方法总接口。
        判断折扣策略是否指定，无指定则折扣金额为0。
        否则调用对应的折扣子方法。
        返回折扣后的金额
        """
        if self.policy is None:
            discount = Decimal(0)
        else:
            discount = self.policy(self)  # 如果不为空，则将Order自身的实例化对象传入变量所指的函数进行调用。
        return self.totla - discount

    def __str__(self):
        """
        订单打印方法，客制化打印信息。
        返回折扣前和折扣后的金额
        """
        return f"<Order total:{self.totla:.2f} due:{self.due():.2f}>"


# 函数化策略
def PointsPolicy(order: Order) -> Decimal:
    """
    积分折扣策略，返回折扣额度
    """
    rate = Decimal('0.05')  # 定义折扣率为0.05
    if order.customer.points >= 1000:
        # 判断客户的积分是否大于等于1000
        return order.totla * rate  # 返回购物车总金额*折扣率的折扣额度
    return Decimal(0)


def ItemPolicy(order: Order) -> Decimal:
    """
    商品数量折扣策略，返回折扣额度
    """
    discount = Decimal(0)
    for item in order.cart:  # 循环从购物车中获取每一个Item的订单。
        if item.quantity >= 20:  # 如果数量大于20
            discount += item.itemtotal * Decimal('0.1')  # 则该商品的总额进行折扣额计算，返回折扣额度
    return discount


def CartPolicy(order: Order) -> Decimal:
    """
    购物车折扣策略，返回折扣额度
    """
    rate = Decimal('0.07')
    distinct_item = {item.product for item in order.cart}  #集合推导式 从购物车中循环取出Item，将Item的商品名称构造入集合
    # 利用集合中项不重复的特性排重
    if len(distinct_item) >= 10:  # 如果不同商品数大于10
        return order.totla * rate  # 返回购物车总金额*折扣率的折扣额度
    return Decimal(0)


def BestPolicy(order: Order) -> Decimal:
    """自动获取最佳折扣信息方法"""

    # 先定义类型，因为函数策略实现模式没有策略类。
    #所有策略函数都是Callbale，并且传递一个Order类型的参数，返回Decimal
    Policy = Callable[['Order'], Decimal]

    # 将策略名加入列表
    policies: list[Policy] = [PointsPolicy, ItemPolicy, CartPolicy]
    # 此代码目前的缺点是不能自动获取子策略函数并生成列表。
    return max(policy(order) for policy in policies)  # 从policies中遍历策略方法，并执行调用传入order对象，
    # 并利用max函数获取最大折扣值


if __name__ == "__main__":
    """测试代码"""
    xueqin = Customer("xueqin", 0)
    haizhenyu = Customer("haizhenyu", 1000)
    cart = (LineItem("banana", 4, Decimal('.5')),
            LineItem("Apple", 20, Decimal('1.5')),
            LineItem("watermelon", 5, Decimal(5)))

    print(Order(xueqin, cart=cart, policy=BestPolicy))
    print(Order(haizhenyu, cart=cart, policy=BestPolicy))
    print(Order(haizhenyu, cart=cart, policy=PointsPolicy))
