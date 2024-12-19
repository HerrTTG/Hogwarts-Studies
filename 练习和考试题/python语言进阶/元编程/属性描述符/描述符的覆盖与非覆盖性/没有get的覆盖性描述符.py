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

# 在托管实例赋值前，查看托管实例的属性over_no_get，返回的是Managed的类属性，引用的描述符对象
print(customer.over_no_get)

# 对属性赋值，调用的确实是描述符类的set方法,但是并没有给托管实例中创建储存属性
customer.over_no_get = 1

# 托管实例重新尝试获取属性，发现返回的依然是描述符对象，并且托管实例属性字典不存在数据
# 因为并没有储存属性
print(customer.over_no_get)
print(vars(customer))

# 绕过__set__方法，直接对托管实例的属性字典进行更新
customer.__dict__["over_no_get"] = 2

# 然后再赋值，会调用描述符的__set__方法
customer.over_no_get = 3

# 但是托管实例再次获取属性时，已经是从托管实例的属性字典中获取结果了
# 并且上述赋值，没有覆盖托管实例属性
print(customer.over_no_get)
print(vars(customer))
