class A:
    def __init__(self):
        print('构造A')

class B1(A):
    def __init__(self):
        super().__init__()
        print('构造B1')

class B2(A):
    def __init__(self):
        super().__init__()
        print('构造B2')

class C(B1,B2):
    def __init__(self):
        super().__init__()
        print('构造C')

c=C()

print(C.mro())