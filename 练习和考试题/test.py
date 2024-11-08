class Des():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.name]
        else:
            return self


class Tuoguan():
    abc = Des()


customer = Tuoguan()

customer.abc = 1
print(customer.abc)
print(vars(customer))

customer.abc = 2
print(customer.abc)
print(vars(customer))
