class UserStr(str):
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return super().__add__(other)
        else:
            return int(self) + other


a = UserStr("12")
print(f"{a}+1={a + 1}")
