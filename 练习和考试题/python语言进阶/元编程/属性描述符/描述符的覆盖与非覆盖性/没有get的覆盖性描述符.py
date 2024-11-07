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


class OverridingNoGet:  # <3>
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class Managed:  # <5>托管类，把所有描述符都构造一遍实例
    over_no_get = OverridingNoGet()

    def spam(self):  # <6>
        print(f'-> Managed.spam({display(self)})')


customer = Managed()

# 查看托管对象的属性over_no_get，发现返回的是描述符对象
print(customer.over_no_get)

# 对属性赋值，调用的确实是set方法
customer.over_no_get = 1

# 重新尝试获取实例属性，发现返回的依然是描述符对象，并且实例属性字典不存在数据
print(customer.over_no_get)
print(vars(customer))

# 更新字典检查
customer.__dict__["over_no_get"] = 2
customer.over_no_get = 3
print(customer.over_no_get)
print(vars(customer))
