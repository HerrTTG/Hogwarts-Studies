from typing import Iterable


def filed(names: str | Iterable[str]):
    if isinstance(names, str):
        names = names.replace(',', '').split()
    # 如果不是一个字符串,说明传入的是一个可迭代对象，故检查可迭代对象每一个项是否符合标识符规则。如果有不合规的，抛出异常
    elif not all(s.isidentifier() for s in names):
        raise ValueError
    return tuple(names)


def factory(class_name: str, filed_names: str | Iterable[str]) -> type:
    slots = filed(filed_names)  # self.__slots__属性

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))  # zip打包__slots__元组中的key，配合传入args位置参数作为字典生成
        attrs.update(kwargs)  # 关键字传入的不能漏

        # 遍历这个字典，对实例化对象属性赋值，相当于self.key=value
        for key, value in attrs.items():
            setattr(self, key, value)

    def __iter__(self):
        """
        对self迭代的实现
        """
        for name in self.__slots__:
            yield getattr(self, name)

    def __str__(self):
        # zip将两个迭代对象进行关联，对slef.__slots__中迭代他本身是个元组。
        # 对self迭代走的是self.__iter__，根据上诉实现的方法，返回的是key对应的属性值。
        # 最后zip把他们的返回值打包成一个元组(name,value)
        values = ','.join(f'{name}={value!r}' for name, value in zip(self.__slots__, self))
        cls_name = self.__class__.__name__
        return f'{cls_name}({values})'

    cls_attrs = dict(__slots__=slots, __init__=__init__, __iter__=__iter__, __str__=__str__)

    return type(class_name, (object,), cls_attrs)


Bil = factory('Dog', "name weight owner")("Bil", 20, owner='Bob')
print(Bil)
