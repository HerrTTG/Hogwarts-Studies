class Car():
    def __init__(self,numb,cartype):
        self.numb=numb
        self.cartype=cartype
    def start(self):
        print('原神启动')

    def end(self):
        print('Op 关闭')


class Tixe(Car):
    def __init__(self,numb,cartype,owner):
        super().__init__(numb,cartype)
        self.ogr=owner
    def start(self):
        print(f'我是出租车，我的车牌号是{self.numb},车型是{self.cartype}.我是{self.ogr}公司的。')

class Selfcar(Car):
    def __init__(self,numb,cartype,owner):
        super().__init__(numb,cartype)
        self.person=owner
    def start(self):
        print(f'我是私家车，我的车牌号是{self.numb},车型是{self.cartype}.车是属于{self.person}的。')




if __name__=='__main__':
    t=Tixe('苏A8888','宝马','牛逼cause公司')
    s=Selfcar('苏A666666','保时捷','王思聪')

    t.start()
    s.start()

