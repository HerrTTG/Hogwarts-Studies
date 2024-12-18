"""
此案例处理数据：
{
  "Schedule": {
    "conferences": [
      {
        "serial": 115
      }
    ],
    "events":[...],
    "speakers":[...],
    "venues":[...]

conferences events speakers venues 对应的列表中都有个关键字serial
如下案例

 "events": [
      {
        "serial": 34505,
        "name": "Why Schools Don´t Use Open Source to Teach Programming",
        "event_type": "40-minute conference session",
        "time_start": "2014-07-23 11:30:00",
        "time_stop": "2014-07-23 12:10:00",
        "venue_serial": 1462,
        "description": "Aside from the fact that high school programming...",
        "website_url": "http://oscon.com/oscon2014/public/schedule/detail/34505",
        "speakers": [
          157509
        ],
        "categories": [
          "Education"
        ]
      }
    ],
    ...
 "venues": [
      {
        "serial": 1462,
        "name": "F151",
        "category": "Conference Venues"
      }
    ]

"""
# tag::SCHEDULE1[]
import json
from inspect import isclass

JSON_PATH = 'E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\python语言进阶\元编程\osconfeed-sample.json'


class Record:
    """
    此类构造对象的同时，将字典转化为对象的属性。
    """
    __index: dict[str:object] = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # <1> 最重要的一步，__dict__字典储存着对象的属性。
        # kwargs关键字，如name="Robert Lefkowitz"，更新进去，作为属性的一部分。
        # 此时对象就拥有了self.name这个属性

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'  # <2>

    @classmethod
    def fetch(cls, key, path=JSON_PATH) -> dict[str:object]:
        """
        该方法对整体字典进行过滤。


        1.用于筛选conferences events speakers venues 中的任意一个key和key对应的vaule值。
        格式为：key.serial
        例:event.34505
        从整体字典字典中获取索引值。Record.__index["event.34505"]
        2.用于在第一次类属性为空时，构造整体字典属性化
        """
        if cls.__index is None:
            cls.__index = load(path)
        return cls.__index[key]


class Event(Record):
    def __repr__(self):
        """
        尝试获取当前页签内的name属性，如果不存在，则交给父类解决打印。
        """
        try:
            return f"<{self.__class__.__name__}{self.name!r}>"
            ##self.__class__ 用于访问当前实例 (self) 的类
            ##原因是.index字典中的项的对象，可能是record构造，也可能是event
            ##目的是Event构造的对象，在打印的时候显示的是<Event...>
        except AttributeError:
            return super().__repr__()

    @property
    def venue(self) -> object:
        """
        特性，让event对象event.venue变成一个属性。其值为该函数的返回值。

        从event属性中获取venue_serial，拼接为key
        并返回返回过滤方法的结果
        """
        # 拼接venue.serial的值，用于索引整体列表。
        key = f'venue.{self.venue_serial}'
        return self.__class__.fetch(key)


def load(path=JSON_PATH) -> dict[str:Record]:
    records = {}  # <3>整体字典先构造为空
    with open(path) as fp:
        source_data = json.load(fp)  # <4>打开文件

    for keys, list in source_data['Schedule'].items():  #
        # <5>keys 是conferences events speakers venues这些keys，他们的项都是一个列表
        # list 就是他们对应的列表
        record_type = keys[:-1]  # <6>拼接新的keyname，去掉s 从events-》event
        cls_name = record_type.capitalize()  # 将key命的首字母大写，从event-》Event

        # 从全局类的字典中，尝试获取cls_name，默认为Record
        cls = globals().get(cls_name, Record)
        if isclass(cls) and issubclass(cls, Record):
            # 还是判断cls是不是一个类，并且是Record的子类，这里暗指Event、Speaker等可能创建的子类
            factory = cls
        else:
            factory = Record
        # 这几步的作用是检查keys们是否定义了对应的名称的子类，如果有，则构造的类使用子类，因为子类可能有独特的特性。
        # 如果没有，那还是用record类来构造

        for rocord in list:
            # <7>字典的key进行拼装，将speakers下的列表中的serial值取出，
            # 拼装为speaker.157509
            new_key = f'{record_type}.{rocord["serial"]}'
            # <8>整体字典更新，映射的vaule是Record对象，将rocord拆包传入。rocord是字典，拆包为key=value给Record进行构造。
            records[new_key] = factory(**rocord)

    return records


# end::SCHEDULE1[]


# 测试代码
if __name__ == "__main__":
    event = Record.fetch("event.34505")  # 赋值event变量，引用Record对象中过滤后的对象。

    # # 获取event下本身的属性
    # print(event)#由Event类创建的对象，所以打印的结果为<Event...>
    # #event下自己的属性
    # print(event.venue_serial)
    # print(event.description)

    # 获取链接的属性
    # Event下定义了一个特性venues 用于获取venues表头下的内容
    print("----------")
    print(event.venue)  # 访问特性，特性返回的是关联的venue表头内的内容所创建的Record对象
    print(event.venue.name)  # 该对象有venue下的所有属性。
    print(event.venue.category)
