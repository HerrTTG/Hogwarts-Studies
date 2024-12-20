from collections.abc import Callable  # <1>
from typing import Any, NoReturn, get_type_hints


class Field:
    """
    描述符类
    """

    def __init__(self, name: str, constructor: Callable) -> None:  # <2>
        # constructor是name属性的类型提示
        # 所以先检查constructor是否是可调用的，或者他是一个None
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


# end::CHECKED_FIELD[]


# tag::CHECKED_TOP[]
class Checked:
    @classmethod
    def _fields(cls) -> dict[str, type]:  # <1>
        """
        get_type_hints 是 Python 3.5 及以上版本提供的一个函数
        它位于 typing 模块中，用于返回一个字典，包含函数的所有参数和返回值的类型注解。
        这里是在获取cls类里的所有属性，方法以及其类型注释
        """
        return get_type_hints(cls)

    def __init_subclass__(subclass) -> None:  # <2>在定义当前类的子类时会被调用,所以会在实例被创建前就执行，相当于装饰器
        super().__init_subclass__()  # <3>交给super去解决继承可能出现的问题，执行某一个该执行的__init_subclass__

        # <4>获取subclass类中的属性和方法，及其类型注释
        # name为subclass中定义的属性名，constructor是他对应的注解
        for name, constructor in subclass._fields().items():
            # <5>在subclass上创建属性名，并赋值指向的是Fiedld这个描述符对象
            # 相当于是程序帮subclass的托管属性上关联了一波描述符对象。
            setattr(subclass, name, Field(name, constructor))

    def __init__(self, **kwargs: Any) -> None:
        ##movie这个子类在被构造的时候执行
        for name in self._fields():  # <6>还是从类属性中获取属性名
            # <7>从kwargs字典中根据key name取出值，并赋值给value，同时删除这一条记录，如果没找到，则返回...
            # 也就是说Moive中定义的类属性，构造时没有关键字传进来
            value = kwargs.pop(name, ...)
            setattr(self, name, value)  # <8>触发__setattr__特殊方法
        if kwargs:  # <9>
            self.__flag_unknown_attrs(*kwargs)  # <10>

    # end::CHECKED_TOP[]

    # tag::CHECKED_BOTTOM[]
    def __setattr__(self, name: str, value: Any) -> None:  # <1>
        """

        """
        # 判断属性是否是之前在init_subclass中已经绑定过描述符对象的托管属性
        if name in self._fields():  #
            # 获取对象的类属性，也就是Movie.name。是指向的描述符对象。
            descriptor = getattr(self.__class__, name)
            # 这里必须这样显示的调用描述符对象的__set__方法。因为一切对self对象的赋值操作都被__setattr__拦截了
            descriptor.__set__(self, value)
        else:
            # 不在_fields返回的结果里，说明是未知属性，转交__flag_unknown_attrs处理
            self.__flag_unknown_attrs(name)

    def __flag_unknown_attrs(self, *names: str) -> NoReturn:  # <5>
        plural = 's' if len(names) > 1 else ''
        extra = ', '.join(f'{name!r}' for name in names)
        cls_name = repr(self.__class__.__name__)
        raise AttributeError(f'{cls_name} object has no attribute{plural} {extra}')

    def _asdict(self) -> dict[str, Any]:  # <6>
        """
        这是一个为了对象打印时，将对象属性和属性值变为映射类型的函数
        直接返回一个字典推导式
        """
        return {
            name: getattr(self, name)
            for name, value in self.__class__.__dict__.items()
            if isinstance(value, Field)
        }

    def __repr__(self) -> str:  # <7>
        kwargs = ', '.join(
            f'{key}={value!r}' for key, value in self._asdict().items()
        )
        return f'{self.__class__.__name__}({kwargs})'


# end::CHECKED_BOTTOM[]

class Movie(Checked):
    title: str
    year: int
    box_office: float


movie = Movie(title='The Godfather', year=1972, box_office=137)
