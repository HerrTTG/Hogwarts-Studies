import numpy as np

a = np.arange(12)
print(a)
print(type(a))
print(a.shape)  # 查看对象的属性shape来看数组的纬度

# 改变数组的纬度
# 增加一个纬度，变成3行4列元素
a.shape = (3, 4)
print(a)
print(a[2])  # 索引查看，也是纬度改变后的数组。

# 行列交换数组，会创建一个新的数组
print(a.transpose())
print(a)
