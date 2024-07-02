from realsubject import RealSubject
from subject import Subject


class Proxy(RealSubject, Subject):
    # 代理类，
    # 父类Subject是一个抽象基类，作为虚拟接口

    def __init__(self, ):
        print("代理先创建real接口的对象，在用父类进行构造")
        super().__init__()

    def givegift(self, name):
        # mix in 的设计方法，直接让代理类继承RealSubject。并至于最左边。
        # super().givegift(name) 会被父类RealSubject拦截，而不是去执行抽象基类Subject 的givegift方法
        super().givegift(name)
