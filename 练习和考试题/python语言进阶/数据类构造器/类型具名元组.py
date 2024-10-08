import typing

# typing.NameTuple 和namedtuple具有一样的功能，只是可为各个字段添加类型注释

Mydata3 = typing.NamedTuple("Mydate3", [('x', int), ('y', int)])
# 亦可以写作 typing.NamedTuple("Mydate3",x=int,y=int)


d = Mydata3(50, 100)
print(d)
# get_type_hints方法会标出元素的数据类型是什么。
print(typing.get_type_hints(d))

# 另外类型标注只是标注，并不会限制用户“违规”,详见类型提示
e = Mydata3("123", 4)
print(e)
# 可以使用asdict方法转为字典
print(e._asdict())


class Mydata4(typing.NamedTuple):
    # NamedTuple 也支持在用户类中直接定义
    # 并且支持定义默认值
    x: int = 0
    y: int = 0

    # class中的使用让代码可读性更高，而且方便覆盖和新填自定义方法
    # 如自定义str方法来展示
    # 使Mydate4(x=0,y=0)变成(x=0,y=0)
    def __str__(self):
        return f"(x={self.x},y={self.y})"


f = Mydata4(50, 100)
print(f)

# 要注意的是Mydaya4 并不是继承自NamedTuple，而是tuple。原因是NamedTuple使用元类这一高级功能创建子类
print(issubclass(Mydata4, tuple))
# _fields方法查看字段名称和默认值
print(Mydata4._fields)
print(Mydata4._field_defaults)
e1 = e._replace(x=123)
print(e1)
