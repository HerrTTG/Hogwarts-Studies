# tag::EXPLORE0[]
from collections import abc

import keyword


class FrozenJSON:
    """
    FrozenJSON实例可嫩使用属性表示法遍历嵌套的字典。
    亦可以使用底层字典的方法如.keys()
    """

    def __new__(cls, arg):
        """
        利用new来进一步优化构造的过程。
        替代build类方法。
        """
        if isinstance(arg, abc.Mapping):
            # 如果是字典，则继续用FrozenJSON这个类进行构造实例
            return super().__new__(cls)  # 这里委托的是object.__new__(FrozenJSON)

        elif isinstance(arg, abc.MutableSequence):
            # 如是字典，则构造一个字典，并遍历字典内的所有项，项交给FrozenJSON(item)继续构造
            return [cls(item) for item in arg]
        else:
            # 返回对象本身
            return arg

    def __init__(self, mapping):
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
        for item, value in mapping.items():
            if keyword.iskeyword(item):
                item += '_'
            self.__data[item] = value

    def __getattr__(self, name):  # <2>
        """
        这个类的关键就是这个方法。
        __getattr__方法当且仅当要获取的属性 在实例化属性，类或者超类中找不到时才会执行

        例如在这个案例中这个类的实例化对象obj并不存在.keys()这个方法(属性)
        就会调用__getattr__ 方法.name为keys()
        """
        try:
            return getattr(self.__data, name)  # <3>而self.__data是一个字典，他是存在keys() 或者item()这些属性的。
            # 所以先尝试交给字典(超类)去处理
        except AttributeError:
            # 如果超类也没有这个属性，那则可能尝试获取的属性是字典的索引
            # 如feed.Schedule
            # 其实就是feed["Schedule"]
            # Schedule这个属性在dict中是不存在的，则走到这一步异常
            # return FrozenJSON.build(self.__data[name])# <4>将字典索引对应的项，交给类方法去重新构造。
            # 重新构造的原因是项可能是一个继续堆叠的字典、或者列表。如{"speakers":[{"name":...},...]}
            # 对他们也构造实例化对象，让其也可以使用获取属性的方法，获取他们内部的项

            # 直接构造新的FrozenJSON对象，而不是调用bulid
            return FrozenJSON(self.__data[name])

    def __dir__(self):  # <5>
        return self.__data.keys()

    # @classmethod
    # def build(cls, obj):  # <6>
    #     if isinstance(obj, abc.Mapping):  # <7>判断如果对象是一个字典，则继续构造新的FrozenJSON对象并返回该对象
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):  # <8>如果对象是一个序列，则遍历其内部的项进行构造FrozenJSON对象，
    #         # 生成一个由FrozenJSON对象组成的列表返回。
    #         return [cls.build(item) for item in obj]
    #     else:  # <9>既不是列表也不是字典，那就原封不动的返回对象(str或者int)
    #         return obj


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
