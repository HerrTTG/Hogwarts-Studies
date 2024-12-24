from collections.abc import Callable  # <1>
from copy import copy
from typing import Any, NoReturn


class Field:
    """
    描述符类
    """

    def __init__(self, name: str, constructor: Callable) -> None:  # <2>
        # constructor是name属性的类型提示
        # 所以先检查constructor是否是可调用的
        if not callable(constructor) or constructor is type(None):  # <3>
            raise TypeError(f'{name!r} type hint must be callable')
        self.name = name
        self.constructor = constructor

    def __set__(self, instance: Any, value: Any) -> None:
        if value is ...:  # <4>如果value为...说明构造的时候未传值。
            # 所以调用constructor()来获取执行类型的默认值。即int()=0 float()=0.0
            value = self.constructor()
        else:
            try:
                value = self.constructor(value)  # <5>对value进行类型转换，相当于int(value)
            except (TypeError, ValueError) as e:  # <6>如果失败，说明构造时传入的value是不符合Movie定义的类型提示的。
                type_name = self.constructor.__name__
                msg = f'{value!r} is not compatible with {self.name}:{type_name}'
                raise TypeError(msg) from e

        instance.__dict__[self.name] = value  # <7>将value值更新到instance的属性字典中


# 装饰器函数
def checked(cls: type) -> type:  # <1>
    # 类属性和类方法定义方法
    for name, constructor in cls.__annotations__.items():  # <2>还是从cls的类属性及其类型注释字典中遍历类属性和类型
        setattr(cls, name, Field(name, constructor))  # <3>将这些类属性名，赋值为描述符实例。
        # 注意此时setattr实例方法还未创建
    # cls._fields = classmethod(_fields)  # type: ignore  # <4>

    # 实例对象方法定义
    # instance_methods元组里都是函数对象，
    instance_methods = (
        __init__,
        __repr__,
        __setattr__,
        # _asdict,
        __flag_unknown_attrs,
    )
    for method in instance_methods:  # <6>
        # 将给实例对象用的方法赋值给类，cls.__init__=__init__函数对象
        setattr(cls, method.__name__, method)

    return cls  # <7>类装饰器必须返回的是个类，实际上装饰器只是起到把cls装饰修改了一番，然后在返回它


#
# def _fields(cls: type) -> dict[str, type]:
#     return get_type_hints(cls)

# 实例方法定义，和在class中写的完全一致
def __init__(self, *args: Any, **kwargs: Any) -> None:
    ##movie这个子类在被构造的时候执行

    if len(args) + len(kwargs) > len(self.__annotations__):
        self.__flag_unknown_attrs(len(args) + len(kwargs))

    # 先处理位置参数，从__annotations__中获取属性名，和位置参数绑定为映射
    attrs = dict(zip((name for name in self.__annotations__), args))
    for name, value in attrs.items():
        setattr(self, name, value)

    # 处理关键字参数
    # 先copy一个新字典，因为在迭代的同时修改迭代对象是不准许的
    _tmp = copy(kwargs)
    for name in kwargs:
        # 判断如果key在类属性名中
        if name in self.__annotations__:
            # 则无论是否需要赋值，都使用pop取出值。
            value = _tmp.pop(name, ...)
            # 判断属性名是否已经是实例化属性
            if isinstance(getattr(self, name), Field):
                setattr(self, name, value)  # <8>对实例属性赋值
    else:
        if _tmp:  # <9>关键字检查完还有剩余的说明是多余的不能接受的属性
            # 因为只要关键字key在类属性名中，无论是否赋值，都会被pop取出。只有不在类属性名中的会被保留
            self.__flag_unknown_attrs(_tmp)  # <10>

    # 处理默认值，对于没有实例化的属性，赋予默认值
    for name in self.__annotations__:
        if isinstance(getattr(self, name), Field):
            setattr(self, name, ...)  #


def __setattr__(self, name: str, value: Any) -> None:  # <1>
    """
      必须显式调用描述符实例的set方法。因为当前实例的所有赋值都会被本函数拦截。
    """
    # 还是要判断name是否在类属性名中定义，这是因为init后，可能用户会对实例属性进行修改
    # 而我们要求不能新增未定义的属性
    # 这也是为什么要实现__setattr__，所有对属性的赋值都需要先经过它进行判断。
    # 对符合定义的转交__set__处理

    if name in self.__annotations__:
        # 获取对象的类属性，也就是Movie.name。是指向的描述符对象。
        descriptor = getattr(self.__class__, name)
        # 这里必须这样显示的调用描述符对象的__set__方法。因为一切对self对象的赋值操作都被__setattr__拦截了
        descriptor.__set__(self, value)
    else:
        # 对于不在类属性定义中的，转交其他函数处理
        self.__flag_unknown_attrs(name)


def __flag_unknown_attrs(self, names: dict | str | int) -> NoReturn:  # <5>
    # 不正确参数检测

    if isinstance(names, dict):
        plural = 's' if len(names) > 1 else ''
        extra = ', '.join(f'{name!r}' for name in names)
    elif isinstance(names, int):
        raise AttributeError(f"{self.__class__.__name__} takes {len(self.__annotations__)} arguments,"
                             f" but give {names}")
    else:
        plural = ''
        extra = names
    cls_name = repr(self.__class__.__name__)
    raise AttributeError(f'{cls_name} object has no attribute{plural} {extra}')


# def _asdict(self: Any) -> dict[str, Any]:
#     return {
#         name: getattr(self, name)
#         for name, attr in self.__class__.__dict__.items()
#         if isinstance(attr, Field)
#     }

def __repr__(self) -> str:  # <7>

    # 从self.__class__.__dict__获取类属性，如果类属性是Filed对象，则拼装key=getattr(self,key)
    # 这里必须这么写，目的是根据定义的类属性名，返回对应的实例属性.
    msg = ', '.join(
        f'{key}={getattr(self, key)!r}'
        for key, value in self.__class__.__dict__.items()
        if isinstance(value, Field)
    )
    return f'{self.__class__.__name__}({msg})'


# end::CHECKED_METHODS[]


# 写法改变了，不在是继承checked。
@checked
class Movie():
    title: str
    year: int
    box_office: float


if __name__ == "__main__":
    movie = Movie('The Godfather', year=2024, box_office=123)
    print(movie)
