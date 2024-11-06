class Descriptor:
    def __get__(self, instance, owner):
        print("Descriptor __get__ called")
        return 42

    def __set__(self, instance, value):
        print("Descriptor __set__ called with", value)

    def __delete__(self, instance):
        print("Descriptor __delete__ called")


class MyClass:
    attr = Descriptor()  # 使用描述符

    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)  # 调用基类的 __getattribute__

    def __setattr__(self, name, value):
        print(f"__setattr__ called for {name} with value {value}")
        super().__setattr__(name, value)  # 调用基类的 __setattr__

    def __delattr__(self, name):
        print(f"__delattr__ called for {name}")
        super().__delattr__(name)  # 调用基类的 __delattr__


obj = MyClass()
print(obj.attr)  # 调用 Descriptor.__get__，而不是 __getattribute__
obj.attr = 100  # 调用 Descriptor.__set__
del obj.attr  # 调用 Descriptor.__delete__
