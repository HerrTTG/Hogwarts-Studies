# 数据类构造器
from collections import namedtuple

# namedtuple 是一个工厂方法，可定义指定的名称和字段来构建一个tuple类的子类

# 工厂方法namedtuple返回一个新的子类Mydata2，并具名两个字段名称x和y
Mydata2 = namedtuple("Mydata2", ['x', 'y'])

# 并且可验证其继承自tuple，拥有和tuple一样的特性
print(issubclass(Mydata2, tuple))

# 测试代码
c = Mydata2(50, 100)
# 和tuple一样，拥有有用的__repr__和__str

# 输出结果清晰可见Mydata2(x=50, y=100)
print(c)

# 可进行运算，无需一一比对实例对象的属性
# 有意义的__eq__
print(c == Mydata2(x=50, y=100))
