class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y


class B(C):
    def __init__(self,x,y,z):
        C.__init__(self,x,y)
        self.z=z
    def add(self):
        return C.add(self)+self.z


b=B(1,2,3)
print(b.add())