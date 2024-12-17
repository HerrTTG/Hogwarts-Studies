# tag::EXPLORE0[]
import keyword
from typing import Mapping, MutableSequence


class FrozenJSON:
    """
    FrozenJSON实例可嫩使用属性表示法遍历嵌套的字典。
    亦可以使用底层字典的方法如.keys()
    """

    def __new__(cls, value):
        """
        利用new来进一步优化构造的过程。
        替代build类方法。
        """
        if isinstance(value, Mapping):
            # 如果是字典，则继续用FrozenJSON这个类进行构造实例
            return super().__new__(cls)
            # 这里委托的是object.__new__(FrozenJSON)来构造一个FrozenJSON对象并返回

        elif isinstance(value, MutableSequence):
            # 如是序列，构造序列，并遍历字典内的所有项，项交给FrozenJSON(item)继续构造
            return [cls(index) for index in value]
        else:
            # 返回对象本身
            return value

    def __init__(self, value):
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
        for item, value in value.items():
            if keyword.iskeyword(item):
                item += '_'
            self.__data[item] = value

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
            return self.__class__(self.__data[attrname])
            # 将字典索引对应的项，交给类方法去判断是否需要重新构造。

    def __dir__(self):  # <5>
        return self.__data.keys()

# end::EXPLORE0[]


import json

with open("E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\python语言进阶\元编程\osconfeed-sample.json") as p:
    feed = FrozenJSON(json.load(p))
#
# print(feed.keys())
# print(feed.Schedule.keys())
# print(dir(feed))
# print(dir(feed.Schedule))
#
# print(feed.Schedule.speakers[-1].name)

a = FrozenJSON({"test": [{"test2": 1}, {"test3": "123"}]})
print(a.test[1].test3)

for i in a.test:
    print(i.items())
