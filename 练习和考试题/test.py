# 动态创建一个类
cls_name = 'MyClass'
bases = (object,)
cls_dict = {'x': 42}

# 使用 type 动态创建类
new_class = type(cls_name, bases, cls_dict)

# 检查创建的类
print(new_class)  # <class '__main__.MyClass'>
print(new_class.x)  # 42

new_class2 = type.__new__(type, cls_name, bases, cls_dict)
print(new_class2)  # <class '__main__.MyClass'>
print(new_class2.x)  # 42
