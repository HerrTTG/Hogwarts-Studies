from subject import Subject


class RealSubject(Subject):

    def __init__(self):
        print("真实实现接口被初始化")
        super().__init__()

    def givegift(self, name):
        print(f"give gift to {name}")
