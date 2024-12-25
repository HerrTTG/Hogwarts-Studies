from collections.abc import Callable
from copy import copy
from typing import Any, NoReturn


# tag::CHECKED_FIELD[]
class Field:
    def __init__(self, name: str, constructor: Callable) -> None:
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f'{name!r} type hint must be callable')
        self.name = name
        self.storage_name = '_' + name  # <1>将储存属性与类属性区分开来
        # 这是因为使用__slots__以后，类属性和实例属性不能同名。
        # 用slots限制instance不能新建slots之外的属性，且用__get__和__set__来拦截独值和设值
        self.constructor = constructor

    def __get__(self, instance, owner=None):
        if instance is None:  # <2>
            return self
        return getattr(instance, self.storage_name)  # <3>因为使用私有储存属性，所以要定制get方法

    def __set__(self, instance: Any, value: Any) -> None:
        """
        描述符的set方法，可以绕过slots，
        对instance设值slots之外的属性。
        __slots__ 限制的是类实例的 公开 属性名称，
        但它并不影响描述符在 __set__ 方法中通过 setattr 动态设置私有属性（如 _title）。
        因此，描述符的 __set__ 方法允许你绕过 __slots__ 的限制，
        向实例添加额外的、不同名称的属性（如 _title），并且这种方式是允许的。
        """
        if value is ...:
            value = self.constructor()
        else:
            try:
                value = self.constructor(value)
            except (TypeError, ValueError) as e:
                type_name = self.constructor.__name__
                msg = f'{value!r} is not compatible with {self.name}:{type_name}'
                raise TypeError(msg) from e
        setattr(instance, self.storage_name, value)
        # 这里不能直接用instance.dict来更新属性了
        # 因为实例被slots限制了，_title是新属性，无法直接更新。
        # 但描述符可以使用 setattr 来动态地设置实例的属性，
        # 而且这个属性不需要再__slots__中。
        # 因此，描述符通过这种方式可以绕过 __slots__ 的限制，动态设置实例的额外属性。


# end::CHECKED_FIELD[]

# tag::CHECKED_META[]
class CheckedMeta(type):

    def __new__(meta_cls, cls_name, bases, cls_dict):  # <1>
        """
        元类其实只干了一件事，读取解析的新类中的类型注释信息。
        并将类属性名+类型。带入Filed中构造描述符实例
        最后加入__slots__中。
        最后交给type.__new__的已经是定制过，拥有类属性绑定描述符实例的新类了。
        """
        if '__slots__' not in cls_dict:  # <2>判断是否有slots属性，只对没有的进行增强。所以基类可以用这种方法逃课。
            # 因为基类不是真正需要定制的家伙。
            # 基类只是携带了元类"基因"同时继承给子类
            # 子类才会执行这个new方法，变成CheckedMeta的实例，基类的子类。
            slots = []
            type_hints = cls_dict.get('__annotations__', {})  # <3>
            for name, constructor in type_hints.items():  # <4>
                field = Field(name, constructor)  # <5>
                cls_dict[name] = field  # <6>
                slots.append(field.storage_name)  # <7>

            cls_dict['__slots__'] = slots  # <8>

        return super().__new__(
            meta_cls, cls_name, bases, cls_dict)  # <9>


# end::CHECKED_META[]

# tag::CHECKED_CLASS[]
class Checked(metaclass=CheckedMeta):
    # 为了不在子类暴露元类，所以由基类来承接元类的构造，子类继承基类，也会由CheckedMeta构造

    # 基类跳过对元类的new方法.
    __slots__ = ()  # skip CheckedMeta.__new__ processing

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ##movie这个子类在被构造的时候执行

        # 排除超出规定数量的错误构造
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
                setattr(self, name, value)  # <8>对实例属性赋值
        else:
            if _tmp:  # <9>关键字检查完还有剩余的说明是多余的不能接受的属性
                # 因为只要关键字key在类属性名中，无论是否赋值，都会被pop取出。只有不在类属性名中的会被保留
                self.__flag_unknown_attrs(_tmp)  # <10>

        # 处理默认值，对于没有实例化的属性，赋予默认值
        for name in self.__annotations__:
            if isinstance(getattr(self, name), Field):
                setattr(self, name, ...)  #

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

    def __repr__(self) -> str:  # <7>

        # 从self.__class__.__dict__获取类属性，如果类属性是Filed对象，则拼装key=getattr(self,key)
        # 这里必须这么写，目的是根据定义的类属性名，返回对应的实例属性.
        msg = ', '.join(
            f'{key}={getattr(self, key)!r}'
            for key, value in self.__class__.__dict__.items()
            if isinstance(value, Field)
        )
        return f'{self.__class__.__name__}({msg})'

# end::CHECKED_CLASS[]
