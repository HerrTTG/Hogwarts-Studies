def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overriding:  # <1>
    """a.k.a. data descriptor or enforced descriptor"""

    def __set_name__(self, owner, name):
        """
        python3。6后支持的描述符方法。让描述符类构造时，不在需要传入属性名。效果等同于__init__。
        """
        self.key_name = name

    def __get__(self, instance, owner):
        # number 和 price，它们的实际值存储在实例的 __dict__ 中
        # instance.__dict__[self.key_name]是储存属性
        print_args('get', self, instance, owner)
        return instance.__dict__[self.key_name]

    def __set__(self, instance, value):
        print_args('set', self, instance, value)
        instance.__dict__[self.key_name] = value


class Managed:  # <5>托管类，把所有描述符都构造一遍实例
    over = Overriding()

    def spam(self):  # <6>
        print(f'-> Managed.spam({display(self)})')


customer = Managed()

# 赋值over时 走的还是Overriding.__set__ (描述符对象self，托管类对象customer,value)
customer.over = 1
print(vars(customer))

# 在调用over这个属性的时候，走的是Overriding.__get__ 参数为(描述符对象self，托管类对象customer，和class Managed)
print(customer.over)

# 绕开描述符，直接给托管对象创建实例化对象over，并赋值为2
customer.__dict__["over"] = 2
print(vars(customer))

# 托管对象获取属性依旧走的是Overriding.__get__
print(customer.over)
