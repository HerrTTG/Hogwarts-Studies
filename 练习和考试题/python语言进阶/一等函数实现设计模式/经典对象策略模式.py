"""
假如有个电商网站，制订了以下折扣规则：
1.有1000或者以上积分的客户，每个订单享受5%折扣。
2.同一订单中，单个商品的数量达到20个或以上，享10%折扣。
3.订单中不同商品的数量达到10个或者以上，享7%折扣。

完全面向对象的方法实现，并增加了类装饰器和实现了自动注册策略，自动获取最佳折扣


"""


from abc import ABC, abstractmethod
from collections.abc import Sequence
from functools import lru_cache
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    """
    客户类：
    客户类是一个具名元组，用来封装客户对象的具名属性。分别是客户name和积分points
    """
    name: str
    point: int | float


class Item(NamedTuple):
    """
    商品类：
    商品类也是一个具名元组，封装客户购买的商品姓名，数量，和单价。并提供一个缓存特性返回该商品对象的总价。。
    """
    product: str
    number: int | float
    price: int | float

    @property
    @lru_cache
    def itemtotal(self) -> int | float:
        return self.number * self.price

class Order(NamedTuple):
    """
    订单类也是一个具名元组，它分别拥有客户属性（来自于客户类的对象）
    购物车属性（商品类的对象产生的列表）
    折扣属性，来自于策略类的对象。
    提供一个汇总购物车总价的特性，返回商品类对象的总价的合计值。
    提供一个内部方法，计算折扣。
    实现__str__方法，格式化输出结果，并自动调用内部方法计算折扣
    """

    customer: Customer
    items: Sequence[Item]
    policy: Optional['Policys'] = None

    @property
    @lru_cache
    def total(self) -> int | float:
        # sum函数的第一个位置传入一个生成器推导式来进行迭代，将每个商品的总价进行累加，从0开始
        return sum((item.itemtotal for item in self.items), start=0)

    def __due(self) -> int | float:
        if self.policy is None:
            disocunt = 0
        else:
            #因为discount中要对购物车中的客户信息，商品信息等进行判断，所以传入self对象。
            disocunt = self.policy.discount(self)
        return self.total - disocunt

    def __str__(self):
        return f"<Order total:{self.total:.2f} Disocunt:{self.__due():.2f}>"


class Policys(ABC):
    """
    策略类的抽象基类
    定义策略的行为和参数。
    """

    @abstractmethod
    def discount(self, order: Order) -> int | float:
        pass


class PolicyRegister:
    """
    策略的注册装饰器。
    __init__实现参数化装饰器，来控制装饰器是否注册登记这一行为
    __call__完成注册，并更新类属性。
    policy为被注册对象
    此案例中被装饰的是类，所以是所有策略类的类名。
    """
    policyslist = []

    def __init__(self, args: bool = False):
        self.__bool = args

    def __call__(self, policy) -> Policys:
        if self.__bool:
            self.__class__.policyslist.append(policy)
        return policy



class BestPolicy(Policys):
    """
    自动获取最佳折扣值的折扣策略，继承自策略抽象基类。
    从装饰器类属性中迭代被注册的类名，对其进行构造，并调用折扣方法，最终返回最大值。
    所以自身不进行注册。避免递归
    """

    def discount(self, order: Order) -> int | float:
        return max(policy().discount(order) for policy in PolicyRegister.policyslist)


@PolicyRegister(True)
class Pointdiscount(Policys):
    """
    积分折扣策略类，被装饰。
    """

    def discount(self, order: Order) -> int | float:
        if order.customer.point > 1000:
            return order.total * 0.05
        else:
            return 0


@PolicyRegister(True)
class Itemdiscount(Policys):
    """
    单一商品商量折扣策略，被装饰。
    """

    def discount(self, order: Order) -> int | float:
        discount = 0
        for item in order.items:
            if item.number > 20:
                discount += item.itemtotal * 0.1
        else:
            return discount


@PolicyRegister(True)
class Orderdiscount(Policys):
    """
    购物车不同商品数量折扣策略，被装饰。
    """

    def discount(self, order: Order) -> int | float:
        #用集合{}推导式，来排除重复的商品名
        if len({item.product for item in order.items}) > 10:
            return order.total * 0.07
        else:
            return 0



if __name__ == "__main__":
    """测试代码"""
    xueqin = Customer("xueqin", 0)
    haizhenyu = Customer("haizhenyu", 1001)

    cart1 = (Item("banana", 4, 0.5),
             Item("Apple", 21, 1.5),
             Item("watermelon", 5, 5))

    cart2 = (Item("banana", 4, 0.5),
             Item("Apple", 20, 1.5),
             Item("watermelon", 5, 5))

    print(Order(xueqin, items=cart1, policy=BestPolicy()))
    print(Order(haizhenyu, items=cart2, policy=BestPolicy()))
