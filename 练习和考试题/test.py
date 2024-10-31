def make(target_class, some_arg):
    new_object = target_class.__new__(some_arg)
    if isinstance(new_object, target_class):
        target_class.__init__(new_object, some_arg)
    return new_object


x = make("Foo", 'bar')
# 上面的函数解释了下面这个表达式Foo类被实例化的过程
x = Foo("bar")
