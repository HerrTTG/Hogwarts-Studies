# tag::EXPLORE0[]
import keyword
from typing import Mapping, MutableSequence


class FrozenJSON:
    """
    FrozenJSON实例可嫩使用属性表示法遍历嵌套的字典。
    亦可以使用底层字典的方法如.keys()
    """

    def __init__(self, mapping: Mapping):
        """
        处理python关键字，如class
        假如字典是
        {"name":'Bib','class':"3N2B"}
        class是不能直接使用
        obj.class获取这个属性的
        因为class本身是关键字
        所以对其进行一点点修改
        构造时将其改为class_
        就可以使用obj.class_来获取了
        """
        self.__data = {}
        # 从mapping映射中遍历key和value，
        for key, value in mapping.items():
            # 如果key是关键字中的一员，则拼接_在后。
            if keyword.iskeyword(key):
                key += '_'

            # 从新构造一个映射关系
            self.__data[key] = value

    def __getattr__(self, attrname):  # <2>
        """
        这个类的关键就是这个方法。
        __getattr__方法当且仅当要获取的属性 在实例化属性，类或者超类中找不到时才会执行
        """
        try:
            # 先尝试attrname去__data字典中尝试获取属性
            # 例如尝试获取obj.keys()这个方法，由于该类不是字典类，也没有实现keys这个方法。所以会走进getattr中
            # 所以先尝试将attrname交给字典去处理
            return getattr(self.__data, attrname)  #
        except AttributeError:
            # 如果字典也没有这个属性，那则可能尝试获取的属性是字典的索引
            # 如feed.Schedule，字典对象本身肯定是没有这个属性的，所以抛出异常AttributeError
            # 按照设计，feed.Schedule就是将传统的获取方式feed["Schedule"]进行替换
            return self.__class__.build(self.__data[attrname])
            # 将字典索引对应的项，交给类方法去判断是否需要重新构造。


    def __dir__(self):  # <5>
        return self.__data.keys()

    @classmethod
    def build(cls, value):  #
        """
        重新构造字典和列表，使其符合属性的标准
        value是上层字典中key对应的value，也就是项。
        """
        if isinstance(value, Mapping):  #
            # <7>判断如果value还是一个映射类型，则传入FrozenJSON类中构造一个新的对象返回。
            return cls(value)
        elif isinstance(value, MutableSequence):
            # <8>如果value是一个序列，则遍历其内部的项，调用build来判断项是否需要重新构造
            # 返回的还是一个列表，但是组成部分已经变成了，list[FrozenJSON|int|str|float|tuple...]
            return [cls.build(item) for item in value]
        else:  # <9>既不是列表也不是字典，那就原封不动的返回value
            return value


# end::EXPLORE0[]


# 测试代码

if __name__ == "__main__":
    import json

    with open("E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\python语言进阶\元编程\osconfeed-sample.json") as p:
        feed = FrozenJSON(json.load(p))

    # print(feed.keys())#feed是FrozenJSON对象本身不是字典，.keys方法会被转交字典去处理
    # print(feed.Schedule.keys())#feed.Schedule是也是一个FrozenJSON对象，同上
    # # 检查他们的属性，这里因为FrozenJSON定义了__dir__方法,所以返回的其实就是字典的.keys方法的结果。
    # print(dir(feed))
    # print(dir(feed.Schedule))
    # # 这便是字典属性化的效果,对象的属性引用的就是字典同名key所映射的value
    # # 如果value还是一个字典,那则拥有字典的所有方法.

    # #同时,value如果还是个字典,也会变为FrozenJSON,其对应的项如果还是字典,也会变为FrozenJSON对象,且储存在value的属性中.
    # #所以feed是一个字典,Schedule是这个最外层字典中的一个key
    # #Schedule这个key映射的项还是个字典,里面有好几个key.他们也变成了Schedule的属性
    # #如speakers，speakers映射的是一个序列，所以他还是一个序列。但其内部的字典也变为了对应index上的FrozenJSON的属性。
    # #如name
    # #最终一个字典结构，就可以使用属性化的方式来访问了
    # print(feed.Schedule.speakers[-1].name)

    # 我们来逐层看一下这些对象
    print(feed)  # <__main__.FrozenJSON object at 0x011A43F0>
    print(feed.Schedule)  # <__main__.FrozenJSON object at 0x0121D430>
    print(feed.Schedule.speakers)  # [<__main__.FrozenJSON object at 0x0121D450>]
    print(feed.Schedule.speakers[-1])  # <__main__.FrozenJSON object at 0x0121D3F0>
    print(feed.Schedule.speakers[-1].name)  #Robert Lefkowitz
