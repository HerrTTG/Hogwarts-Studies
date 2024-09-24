dial_code = [("country", 'Tokoy'), ("remark", 321)]
new = {i: j for i, j in dial_code}

# new["test"]
# 直接尝试get因为key"test并不存在"，所以会返回KeyError


# 解决办法一：
a = new.get("test", [])
a.append("test in here")
new["test"] = a
print(new)
# 在获取key值的过程中，同时指定默认值，
# 再增加内容
# 最后将引用归入字典


# 解决办法二：
new.setdefault("test1", []).append("test1 in here")
print(new)
# 一步解决，是办法1的高级优化版本


# 解决办法三：
# 直接定义字典的默认项是什么。
# 其他处理如办法一办法二一样，如果key不存在，则调用defaultdict来生成实例，并将引用赋予key上
import collections

new1 = collections.defaultdict(list)
new1["test3"].append("test3 in here")
print(new1)


# 解决办法四：
# 自定义字典类
# missing方法是在字典尝试get key未能获得时，自动调用的。
# 此案例将使dict[123]支持key值传入为非字符串
# 内部的get方法在使用__getitem__尝试获取key时。123显然是获取不到的。
# mssing来进行拦截处理，判断key是否为字符串，如果不是，则先转为字符串在get。
class UserDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        else:
            return self[str(key)]

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

    def get(self, key, default=None):
        try:
            self[key]
        except KeyError:
            return default


b = UserDict()
c = dict()

b["4"] = "test4 in here"
c["4"] = "test4 in here"
print(b[4])
print(c[4])
