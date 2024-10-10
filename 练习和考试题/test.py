def out(func):
    def inner(*args, **kwargs):
        print("123")
        func(*args, **kwargs)
        print("end")

    return inner


def ppa(number):
    print(f"i am func {number}")


ppa = out(ppa)
ppa(number=2)
print(ppa.__name__)
