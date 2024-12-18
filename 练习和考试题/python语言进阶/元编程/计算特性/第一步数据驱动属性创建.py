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
        ##kwargs 是一个由key=value组成的关键字收集参数
        self.__dict__.update(kwargs)  # 将kwargs更新给对象的属性值
        # kwargs关键字中有，如name="Robert Lefkowitz"，更新进去，作为属性的一部分。
        # 此时对象就拥有了self.name这个属性，映射"Robert Lefkowitz"

    def __repr__(self):
        """
        打印对象的方法，展示对象类名，和对应的serial属性。
        这里的serial属性一定是init处理过程中动态更新进来的属性。
        """
        return f'<{self.__class__.__name__} serial={self.serial!r}>'  # <2>


def load(path=JSON_PATH) -> dict[str:Record]:
    records = {}  # <3>整体字典
    with open(path) as fp:
        source_data = json.load(fp)  # <4>

    for keys, list in source_data['Schedule'].items():  #
        # <5>keys 是conferences events speakers venues这些keys，他们的项都是一个列表
        # list 就是他们对应的列表
        record_type = keys[:-1]  # <6>拼接新的keyname，去掉s 从speakers-》speaker

        for rocord in list:
            # <7>字典的key进行拼装，将speakers下的列表中的serial值取出，
            # 拼装为speaker.157509
            new_key = f'{record_type}.{rocord["serial"]}'

            # <8>整体字典更新，映射的vaule是Record对象，将rocord拆包传入。rocord是字典，拆包为key=value给Record进行构造。
            records[new_key] = Record(**rocord)

    return records


# end::SCHEDULE1[]

# 测试代码
if __name__ == "__main__":
    record = load(JSON_PATH)  # load函数读取文件，并且将已经构造好对象的整体字典返回。返回类型是dict[str:Record]
    print(record.keys())  # record的中的keys 都变成了拼接好的新key了 如speaker.157509
    speaker = record["speaker.157509"]  # record["speaker.157509"] 索引，映射的项是一个Record对象

    print("---------------------")
    print(speaker)
    print(vars(speaker))  # speaker下的所有key-value都变成了属性化。
    print(speaker.name)
    print(speaker.twitter)
