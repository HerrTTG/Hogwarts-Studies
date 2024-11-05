class Line():
    def __init__(self):
        self.ls = [i for i in range(3)]

    @property
    def member(self):
        return self.ls

    @member.deleter
    def member(self):
        member = self.ls.pop(0)
        print(f"del {member}")


customer = Line()
print(customer.member)
del customer.member
print(customer.member)
