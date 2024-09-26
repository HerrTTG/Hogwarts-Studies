class SubDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = SubDict(a=1)
print(dd)
dd["b"] = 2
print(dd)
dd.update(c=3)
print(dd)
