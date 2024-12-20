from typing import Iterable, Generator


def class_factory(class_name: str, filed_names: str | Iterable[str]) -> type:
    # 下面几个函数，都是定义给类用的方法
    def __init__(self, *args, **kwargs):
        """
        该方法实现self.name=name
                self.weight=weight

        """
        # 位置参数和属性的绑定
        # zip打包__slots__元组中的储存的属性名，配合类传入args位置参数，生成key-value映射字典
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)  # 关键字传入的不能漏

        # 相当于Dog("Bil",20,owner='Bob')
        # args=("Bil",20)
        # kwargs={"owner":'Bob'}
        #最后attrs为这三个属性的映射字典

        # 遍历这个字典，对实例化对象属性赋值，相当于self.key=value
        for key, value in attrs.items():
            setattr(self, key, value)

    def __iter__(self) -> Generator:
        """
        对self迭代的实现
        """
        # 因为__slots__元组中是属性的name，所以遍历的实现就是生成器函数返回对象self的这几个属性。
        for attr_name in self.__slots__:
            yield getattr(self, attr_name)

    def __str__(self) -> str:
        """
        对象的打印实现
        """
        # zip将两个迭代对象进行关联，对slef.__slots__中迭代他本身是个元组。
        # 对self迭代走的是self.__iter__，根据上诉实现的方法，返回的是key对应的属性值。
        # 最后zip把他们的返回值打包成一个元组(name,value)
        values = ','.join(f'{name}={value!r}' for name, value in zip(self.__slots__, self))
        cls_name = self.__class__.__name__
        return f'{cls_name}({values})'

    # self.__slots__类属性,是一个元组('name', 'weight', 'owner')储存的属性名
    # 使用slots 是因为我们希望这个类是一个"元组"，生成后的字段结构不改变。
    # 也就是不能新增属性，不能多一个sex这样的属性。所以这里用slots来管理需要用的到属性名。
    slots = filed_check(filed_names)

    #将类属性和类方法生成字典，可调用对象变为方法，其他变为类属性。
    cls_attrs = dict(__slots__=slots, __init__=__init__, __iter__=__iter__, __str__=__str__)
    return type(class_name, (object,), cls_attrs)


def filed_check(names: str | Iterable[str]) -> tuple[str]:
    if isinstance(names, str):
        names = names.replace(',', '').split()
        # 将字符串中逗号，变为空格，并spilt变为列表
        # "name,eight,owner" => "name weight owner"=>['name', 'weight', 'owner']
    # 如果不是一个字符串,说明传入的是一个可迭代对象，故检查可迭代对象每一个项是否符合标识符规则。如果有不合规的，抛出异常
    elif not all(s.isidentifier() for s in names):
        raise ValueError

    return tuple(names)


# 测试代码
if __name__ == "__main__":
    Bil = class_factory('Dog', "name weight owner")("Bil", 20, owner='Bob')
    Mooe = class_factory('Cat', "name weight age owner")("Mooe", 12, 1, owner='John')
    print(Bil)
    print(Mooe)
