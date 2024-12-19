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


class NonOverriding:  # <4>
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)



class Managed:  # <5>托管类，把所有描述符都构造一遍实例
    non_over = NonOverriding()

    def spam(self):  # <6>
        print(f'-> Managed.spam({display(self)})')


customer = Managed()

# 托管对象未赋值同名属性前，属性的读取还是走描述符方法的
print(customer.non_over)

# 赋值后，托管实例属性覆盖描述符
customer.non_over = 1
print(customer.non_over)

# 描述符对象为普通类属性
print(Managed.non_over)

# 删除托管实例属性，描述符恢复
del customer.non_over
print(customer.non_over)
