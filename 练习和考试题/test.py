def factory(attrname):
    def _getfunc(instance):
        return instance.__dict__[f"_{attrname}"]

    def _setfunc(instance, value):
        instance.__dict__[f"_{attrname}"] = value

    return property(_getfunc, _setfunc)



class Myclass:
    data = factory("data")

    def __init__(self, data):
        self.data = data

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


test = Myclass("123")
print(test.data)
