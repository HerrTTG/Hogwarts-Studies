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
    "speakers": [
      {
        "serial": 157509,
        "name": "Robert Lefkowitz",
        "photo": null,
        "url": "http://sharewave.com/",
        "position": "CTO",
        "affiliation": "Sharewave",
        "twitter": "sharewaveteam",
        "bio": "Robert ´r0ml´ Lefkowitz is the CTO at Sharewave, a startup..."
      }
    ],

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
    def fetch(cls, key, path=JSON_PATH) -> object:
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
        except AttributeError:
            return super().__repr__()

    @property
    def venue(self) -> object:
        """
        特性，让event类构造的对象，能关联到venue
        event中的venue_serial是关联venues中的serial
        当前对象有venue_serial属性，拼装为key.vaule的格式
        转给类的静态方法fetch去筛选结果
        """
        key = f'venue.{self.venue_serial}'
        return self.__class__.fetch(key)

    @property
    def speakers(self) -> list[object]:
        """
        event下的speakers特性因为和Schedule下的speakers重名所以需要特殊处理。
        """
        # 使用一个实例化属性__speaker_objs来储存从speakers获取的内容合集
        if not hasattr(self, '__speaker_objs'):  # event自己的缓存实现，
            sp_serials = self.__dict__["speakers"]  # 直取当前对象下的speakers。即event下的speakers。
            fetch = self.__class__.fetch
            # 给这个私有属性赋值，下次在访问特性的时候，这个私有属性因为已经存在了，就不会再读取一遍fetch而是直接返回结果
            self.__speaker_objs = [fetch(f"speaker.{key}") for key in sp_serials]
        return self.__speaker_objs


def load(path=JSON_PATH) -> dict[str:Record]:
    records = {}  # <3>整体字典先构造为空
    with open(path) as fp:
        raw_data = json.load(fp)  # <4>打开文件

    for collection, raw_records in raw_data['Schedule'].items():  # 从Schedule下取出key，value
        # <5>key-collection 是conferences events speakers venues
        # value-raw_records 是他们对应的列表
        record_type = collection[:-1]  # <6>去掉s speakers-》speaker

        cls_name = record_type.capitalize()  # 将key命的首字母大写，从event-》Event
        cls = globals().get(cls_name, Record)  # 从全局类中获取cls_name 如果存在cls_name这个类
        # 则返回这个类，否则返回Record
        if isclass(cls) and issubclass(cls, Record):
            # 还是判断cls是不是一个类，并且是Record的子类，这里暗指Event、Speaker等可能创建的子类
            factory = cls
        else:
            factory = Record
        # 这几步的作用是检查keys们是否定义了对应的名称的子类，如果有，则构造的类使用子类，因为子类可能有独特的特性。
        # 如果没有，那还是用record类来构造

        # 从values中遍历里面的内容raw_records是一个列表raw_record是字典
        for raw_record in raw_records:
            # 拼装index的格式，为event.serial
            key = f'{record_type}.{raw_record["serial"]}'  # <7>字典的key进行拼装，将speakers下的列表中的serial值取出，
            records[key] = factory(**raw_record)  # <8>字典更新，使用子类或者父类来构造。解包传入key=value的格式。

    return records


# end::SCHEDULE1[]
event = Record.fetch("event.34505")

# 获取event下本身的属性
print(event)
print(event.speakers)

# 获取speakers合集下面的对应属性
print(event.speakers[-1].name)
