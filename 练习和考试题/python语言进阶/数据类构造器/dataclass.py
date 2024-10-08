import dataclasses
import typing


@dataclasses.dataclass(frozen=True)
class Mydata5:
    # 在定义数据类的结构上于继承typing.NamedTuple类类似

    x: int = 0
    y: int = 0

    # 也是可以自定义str方法来展示
    def __str__(self):
        return f"(x={self.x},y={self.y})"


f = Mydata5(50, 100)
print(f)
# dataclass不依赖继承所以issubclass(Mydata4,tuple) 的结果是Fasle
print(issubclass(Mydata5, tuple))
# 使用dataclasses.asdict方法可转为字典格式
print(dataclasses.asdict(f))
# dataclasses.fields查看字段名称和默认值
print(dataclasses.fields(Mydata5))
# 但dataclass数据类，也可以使用typing.get_type_hints 来获取具名的字段类型
print(typing.get_type_hints(f))

f1 = dataclasses.replace(f, x=100)
print(f1)

# 定义一个数据类的描述
# 不像class 会在模块运行前进行构造，dataclasses.make_dataclass构造的类Mydata6只在代码运行到此时此刻时才被定义。
Mydata6 = dataclasses.make_dataclass('Mydata6',
                                     fields=[('x', int), ('y', int)],
                                     init=True,  # 是否自动生成初始化方法，默认True
                                     repr=True,  # 是否自动生成 __repr__ 方法，默认True
                                     eq=True,  # 是否自动生成 __eq__ 方法，默认True
                                     order=False)  # 是否按字段顺序排序，如果order=True则会按照字段顺序排列，否则无序，默认False)

g = Mydata6(x=1000, y=1000)
print(g)
