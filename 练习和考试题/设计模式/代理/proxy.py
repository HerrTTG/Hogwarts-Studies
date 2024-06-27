from realsubject import RealSubject
from subject import Subject


class Proxy(Subject):

    def __init__(self, ):
        print("代理先创建real接口的对象，在用父类进行构造")
        self.who = RealSubject()
        super().__init__()

    def givegift(self, name):
        self.who.givegift(name)
