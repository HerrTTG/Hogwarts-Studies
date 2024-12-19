class CachedDes():
    def __init__(self, func):
        # 被修饰的方法在构造时传入
        self.func = func
        # 拼装一个新的属性名用于储存缓存，注意这里不能直接使用func.__name__
        # 因为托管实例instance是有func.__name__这个属性的。
        self._cache_name = f"_{func.__name__}_cache"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # 缓存实现的代码
        # 判断托管实例中是否有储存属性，如果有，直接返回储存属性的属性值。
        # 否则更新托管实例属性
        if hasattr(instance, self._cache_name):
            return instance.__dict__[self._cache_name]
        else:
            result = self.func(instance)
            instance.__dict__[self._cache_name] = result
            return result


class Myclass:
    def __init__(self, x):
        self.x = x

    @CachedDes
    def cal(self):
        return self.x ** 2


hhh = Myclass(10)
print(hhh.cal)
print(hhh.cal)
