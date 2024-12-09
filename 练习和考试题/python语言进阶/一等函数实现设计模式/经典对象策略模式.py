from abc import ABC, abstractmethod
from collections.abc import Sequence
from functools import lru_cache
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    point: int | float


class Item(NamedTuple):
    product: str
    number: int | float
    price: int | float

    @property
    @lru_cache
    def Itemtotal(self):
        return self.number * self.price

class Order(NamedTuple):
    customer: Customer
    items: Sequence[Item]
    policy: Optional['Policys'] = None

    @property
    @lru_cache
    def total(self):
        return sum((item.Itemtotal for item in self.items), start=0)

    def __due(self):
        if self.policy is None:
            return 0
        else:
            return self.total - self.policy.discount(self)

    def __str__(self):
        return f"<Order total:{self.total:.2f} Disocunt:{self.__due():.2f}>"


class PolicyRegister():
    policyslist = []

    def __init__(self, bool: bool = False):
        self.__bool = bool

    def __call__(self, policy):
        if self.__bool == True:
            self.__class__.policyslist.append(policy)
        return policy


class Policys(ABC):

    @abstractmethod
    def discount(self, order: Order):
        pass


class BestPolicy(Policys):
    def discount(self, order: Order):
        return max(policy().discount(order) for policy in PolicyRegister.policyslist)


@PolicyRegister(True)
class Pointdiscount(Policys):
    def discount(self, order: Order):
        if order.customer.point > 1000:
            return order.total * 0.05
        else:
            return 0


@PolicyRegister(True)
class Itemdiscount(Policys):
    def discount(self, order: Order):
        discount = 0
        for item in order.items:
            if item.number > 20:
                discount += item.Itemtotal * 0.1
        else:
            return discount


@PolicyRegister(True)
class Orderdiscount(Policys):
    def discount(self, order: Order):
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
