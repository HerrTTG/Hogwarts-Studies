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
    ]

    我们想将serial 和他对应的字典关联起来。
    即但我们尝试获取索引speaker.157509时，她返回的是一个对象，一个包含由157509所在的字典所有keyvalue 为对象属性的对象
"""

# tag::SCHEDULE1[]
import json

JSON_PATH = 'E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\python语言进阶\元编程\osconfeed-sample.json'


class Record:
    """
    此类构造对象的同时，将字典转化为对象的属性。
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # <1> 最重要的一步，__dict__字典储存着对象的属性。
        # 将kwargs字典解包，如name="Robert Lefkowitz"，更新进去，作为属性的一部分。
        # 此时对象就拥有了self.name这个属性

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'  # <2>


def load(path=JSON_PATH) -> dict[str:Record]:
    records = {}  # <3>整体字典
    with open(path) as fp:
        raw_data = json.load(fp)  # <4>
    for collection, raw_records in raw_data['Schedule'].items():  #
        # <5>collection 是conferences events speakers venues
        # raw_records 是他们对应的列表
        record_type = collection[:-1]  # <6>去掉s speakers-》speaker
        for raw_record in raw_records:
            key = f'{record_type}.{raw_record["serial"]}'  # <7>字典的key进行拼装，将speakers下的列表中的serial值取出，
            # 拼装为speaker.157509
            records[key] = Record(**raw_record)  # <8>字典更新keyvaule，vaule是Record对象，将raw_record拆包传入。
            # raw_record：
            # {
            #     "serial": 157509,
            #     "name": "Robert Lefkowitz",
            #     "photo": null,
            #     "url": "http://sharewave.com/",
            #     "position": "CTO",
            #     "affiliation": "Sharewave",
            #     "twitter": "sharewaveteam",
            #     "bio": "Robert ´r0ml´ Lefkowitz is the CTO at Sharewave, a startup..."
            # }
    return records


# end::SCHEDULE1[]

record = load(JSON_PATH)
speaker = record["speaker.157509"]  # 索引的是一个Record对象
print(speaker)
print(speaker.name)
print(speaker.twitter)
