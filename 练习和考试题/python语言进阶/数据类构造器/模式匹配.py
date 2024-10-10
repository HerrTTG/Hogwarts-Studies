import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


citys = [City('Asia', 'Tokoy', 'JP'), City('Asia', 'Delhi', 'IN'), City('North America', 'Mexico', 'MX')]


def match_asia_cicies(record: list):
    result = []
    for city in record:
        match city:
            case City('Asia', _, cc):  # 位置匹配
                result.append(cc)
    print(result)


match_asia_cicies(citys)
