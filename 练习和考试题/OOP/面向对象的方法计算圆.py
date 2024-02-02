'''
需求：定义一个圆的类，提供一个属性r（半径），提供两个方法分别计算面积和周长并输出结果。最后键入半径r，创建实例化对象，并调用方法得出结果。
'''
import pyinputplus


class Circle():
    def __init__(self,r):
        self.r=r
    def get_area(self):
        print(3.1415926*pow(self.r,2))
    def get_perimter(self):
        print(2*3.1415926*self.r)



def main():
    r=pyinputplus.inputNum('请输入半径:')
    a=Circle(r)
    a.get_area()
    a.get_perimter()

if __name__ =='__main__':
    main()