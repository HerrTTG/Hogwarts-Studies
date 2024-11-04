a = {"test": 123}


def abc(**kwargs):
    b = {}
    b.update(kwargs)
    return b


print(abc(**a))
