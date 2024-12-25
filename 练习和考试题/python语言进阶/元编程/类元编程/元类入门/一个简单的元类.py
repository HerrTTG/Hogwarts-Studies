class MetaBunch(type):  # <1>
    def __new__(meta_cls, cls_name, bases, cls_dict):  # <2>
        # 只需要改写这一个方法，在交给super().__new__之前。
        # 对cls_name, bases, cls_dict进行一定的修改

        defaults = {}  # <3>用来存放属性名和值的映射

        # 先来定义实例方法
        def __init__(self, **kwargs):  # <4>
            # 实例方法其实也很简单。
            for name, default in defaults.items():  # <5>
                # 在从kwargs中根据属性名取出值，未找到则使用默认值替代
                # 最后对实例属性进行赋值
                setattr(self, name, kwargs.pop(name, default))
            if kwargs:  # <6>
                extra = ', '.join(kwargs)
                raise AttributeError(f'No slots left for: {extra!r}')

        def __repr__(self):  # <7>
            # 实例属性的打印方法
            # 注意这里做了限制，只打印非默认值。
            rep = ', '.join(f'{name}={value!r}'
                            for name, default in defaults.items()
                            # 如果 getattr(self, name) 不等于默认值，则赋值给value
                            if (value := getattr(self, name)) != default)
            return f'{cls_name}({rep})'

        # 拼装新的cls_dict
        new_dict = dict(__slots__=[], __init__=__init__, __repr__=__repr__)  # <8>

        for name, value in cls_dict.items():  # <9>先从原始cls_dict中解析
            if name.startswith('__') and name.endswith('__'):  # <10>捞出特殊方法
                if name in new_dict:
                    # 检查特殊方法是否在new_dict中，这一步其实是在限制使用改元类构造的类，不能实现new_dict中的属性和方法
                    raise AttributeError(f"Can't set {name!r} in {cls_name!r}")
                # 其他特殊方法原封不动的加入new_dict中
                new_dict[name] = value
            else:  # <11>不是特殊方法的，说明是属性，或者自定义方法。加入__slots__中
                new_dict['__slots__'].append(name)
                # 这个案例中被构造的类不需要自定义方法，所以这里不检查value是不是函数对象，默认就是类属性。
                # 所以全部存入
                defaults[name] = value

        return super().__new__(meta_cls, cls_name, bases, new_dict)  # <12>调用type.__new__创造并返回类对象


class Bunch(metaclass=MetaBunch):  # <13>提供一个基类，因此继承的子类无需关心元类
    # 且可以在基类中，重写一些对来自type创造类时注入的实例方法
    pass


class Point(Bunch):
    x = 0.0
    y = 0.0
    color = 'gray'


if __name__ == "__main__":
    p1 = Point(x=1.2, y=3, color='green')
    print(p1)
    p2 = Point()
    print(p2)
    print(p2.x, p2.y, p2.color)
    p2.x = 42
    print(p2)
    p2.newattr = 42
