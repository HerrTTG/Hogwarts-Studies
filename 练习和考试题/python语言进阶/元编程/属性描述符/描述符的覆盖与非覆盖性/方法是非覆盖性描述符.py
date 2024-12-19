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


class Managed:  # <5>托管类，把所有描述符都构造一遍实例
    def spam(self):  # <6>
        print(f'-> Managed.spam({display(self)})')


customer = Managed()

# 用户在读取方法时，找不到实例属性。就会向上寻找到类属性进行调用。
print(customer.spam)

# 创建实例化对象同名属性后将覆盖方法
customer.spam = 7
print(customer.spam)
print(Managed.spam)
