class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y

c=C(2,3)

print(c.add())

print(c.__dict__)