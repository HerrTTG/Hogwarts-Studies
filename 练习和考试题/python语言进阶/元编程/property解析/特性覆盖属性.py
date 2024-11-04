class Line():
    customer = 'test'

    @property
    def data(self):
        return "abc"


customer = Line()
# 实例属性不存在，但是类属性存在，自动获取类属性
print(vars(customer))
print(customer.customer)
print("-----------------")
# 赋值实例化属性实例化属性存在后，获取的就是实例化属性，但类属性不变。
customer.customer = "test2"
print(vars(customer))
print(customer.customer)
print(customer.__class__.customer)
print("-----------------")

# 直接从类属性中获取特性，不会执行特性，而是返回特性的对象
print(customer.__class__.data)  # <property object ....>
# 读值特性
print(customer.data)
print("-----------------")
# 尝试同名实例化属性,提示特性没有设值方法，实例化属性覆盖失败。
try:
    customer.data = '123'
except AttributeError as e:
    print(e)
# 然而可以绕过特性，直接更新对象的实例化属性值,但是读取属性时，还是会优先读取特性的返回值
# 特性未被覆盖
customer.__dict__.update(data='123')
print(vars(customer))
print(customer.data)
print("-----------------")
# 覆盖特性，销户特性的对象，
# 现在读取属性就是实例属性了
customer.__class__.data = 'del'
print(customer.data)
print("-----------------")

# 新增特性
# 实例属性依然在实例属性字典中，但是读取会被特性取代
customer.__class__.customer = property(lambda self: "prop value")
print(vars(customer))
print(customer.customer)
print(customer.__class__.customer)
