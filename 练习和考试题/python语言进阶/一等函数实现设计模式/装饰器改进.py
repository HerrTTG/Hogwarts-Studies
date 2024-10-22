from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional, Callable

##装饰器定义
# 定义Policy变量的全局类为一个可调用对象，且可传参一个Order类的对象，返回Decimal。
# 这里暗指所有符合条件的子策略
Policy = Callable[['Order'], Decimal]

# 全局的策略列表，被装饰器装饰后会将函数对象加入列表中
policies: list[Policy] = []


def PolicyRegister(policy: Policy) -> Policy:
    """
    装饰器函数，在函数被装饰后，在被装饰函数被导入时调用。
    将符合条件的子策略对象，记录进入全局列表policies中。
    起到一个注册被装饰函数对象的作用。
    然后原封不动的返回子策略对象。
    该函数使可能的后续新增的子策略，都会被自动注册。
    解决在BestPolicy中，用列表记录策略函数对象的缺点。
    """
    policies.append(policy)
    return policy



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
    policy: Optional[Policy] = None

    def totla(self):
        """
        获取客户的总购物消费值
        """
        totals = (item.Itemtotal() for item in self.cart)  # 从客户的购物车实例属性序列中取出每一个项，调用项的Itemtotal方法
        return sum(totals, start=Decimal(0))  # 为什么这么写

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
        return self.totla() - discount

    def __str__(self):
        """
        订单打印方法，客制化打印信息。
        返回折扣前和折扣后的金额
        """
        return f"<Order total:{self.totla():.2f} due:{self.due():.2f}>"



def BestPolicy(order: Order) -> Decimal:
    """自动获取最佳折扣信息方法"""
    return max(policy(order) for policy in policies)  # 从被注册装饰器生成的全局policies变量中遍历策略方法，
    # 并执行调用传入order对象，
    # 并利用max函数获取最大折扣值


# 函数化策略
@PolicyRegister
def PointsPolicy(order: Order) -> Decimal:
    """
    积分折扣策略，返回折扣额度
    """
    rate = Decimal('0.05')  # 定义折扣率为0.05
    if order.customer.points >= 1000:
        # 判断客户的积分是否大于等于1000
        return order.totla() * rate  # 返回购物车总金额*折扣率的折扣额度
    return Decimal(0)


@PolicyRegister
def ItemPolicy(order: Order) -> Decimal:
    """
    商品数量折扣策略，返回折扣额度
    """
    discount = Decimal(0)
    for item in order.cart:  # 循环从购物车中获取每一个Item的订单。
        if item.quantity >= 20:  # 如果数量大于20
            discount += item.Itemtotal() * Decimal('0.1')  # 则该商品的总额进行折扣额计算，返回折扣额度
    return discount


@PolicyRegister
def CartPolicy(order: Order) -> Decimal:
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
    haizhenyu = Customer("haizhenyu", 1000)
    cart = (LineItem("banana", 4, Decimal('.5')),
            LineItem("Apple", 20, Decimal('1.5')),
            LineItem("watermelon", 5, Decimal(5)))

    print(Order(xueqin, cart=cart, policy=BestPolicy))
    print(Order(haizhenyu, cart=cart, policy=BestPolicy))
    print(Order(haizhenyu, cart=cart, policy=PointsPolicy))
