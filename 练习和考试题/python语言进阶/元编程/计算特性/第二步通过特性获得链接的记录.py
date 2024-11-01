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
    __index = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # <1> 最重要的一步，__dict__字典储存着对象的属性。
        # 将kwargs字典解包，如name="Robert Lefkowitz"，更新进去，作为属性的一部分。
        # 此时对象就拥有了self.name这个属性

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'  # <2>

    @staticmethod
    def fetch(key, path=JSON_PATH):
        if Record.__index is None:
            Record.__index = load(path)
        return Record.__index[key]


class Event(Record):
    def __repr__(self):
        try:
            return f"<{self.__class__.__name__}{self.name!r}>"
        except AttributeError:
            return super().__repr__()

    @property
    def venue(self):
        key = f'venue.{self.venue_serial}'
        return self.__class__.fetch(key)


def load(path=JSON_PATH) -> dict[str:Record]:
    records = {}  # <3>整体字典
    with open(path) as fp:
        raw_data = json.load(fp)  # <4>
    for collection, raw_records in raw_data['Schedule'].items():  #
        # <5>collection 是conferences events speakers venues
        # raw_records 是他们对应的列表
        record_type = collection[:-1]  # <6>去掉s speakers-》speaker
        cls_name = record_type.capitalize()  # 变为Event Speaker 来作为类名
        cls = globals().get(cls_name, Record)  # 从全局类中获取cls_name 如果存在这个类，则返回这个类，否则返回Record
        if isclass(cls) and issubclass(cls, Record):
            # 还是判断cls是不是一个类，并且是Record的子类，这里暗指Event类
            factory = cls
        else:
            factory = Record
        for raw_record in raw_records:
            key = f'{record_type}.{raw_record["serial"]}'  # <7>字典的key进行拼装，将speakers下的列表中的serial值取出，
            records[key] = factory(**raw_record)  # <8>字典更新keyvaule，vaule是Record对象，将raw_record拆包传入。

    return records


# end::SCHEDULE1[]
event = Record.fetch("event.34505")

# 获取event下本身的属性
print(event)
print(event.venue_serial)
print(event.description)

# 获取链接的属性
# Event下定义了一个特性venues 用于获取venues表头下的内容
print("----------")
print(event.venue)
print(event.venue.name)
print(event.venue.category)
