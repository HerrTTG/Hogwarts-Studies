d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

from collections import ChainMap

chain = ChainMap(d1, d2)
print(chain["a"])
print(chain["b"])
print(chain["c"])

from collections import Counter

ct = Counter("abracadabra")
print(ct)

ct.update("aaaaaazzz")
print(ct)
print(ct.most_common(3))

from types import MappingProxyType

d = {"a": 1}
d_proxy = MappingProxyType(d)
print(d_proxy)
d["a"] = 2
print(d_proxy)
d_proxy["a"] = 3
