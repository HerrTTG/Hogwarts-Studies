'''
作业要求
编写一个Python程序，可以执行加法、减法、乘法和除法操作。
用户可以输入两个数字和运算符，然后计算并输出结果。
实现计算器的功能（+、-、*、/），并处理异常情况，
比如：输入的不是数字、除数为0等。
'''
import pyinputplus

class C:
    def __init__(self):
        self.a,self.b,self.c=C.userinput()

    @classmethod
    def userinput(cls):
        try:
            a=pyinputplus.inputNum('请输入第一个数：',limit=3)
            b=pyinputplus.inputNum('请输入第二个数：', limit=3)
            for i in range(3):
                c = input('请输入操作符：')
                if c in ['+', '-', '*', '/']:
                    break
                else:
                    print('请输入正确的操作符（+、-、*、/）')
                    continue
            else:
                assert c in ['+', '-', '*', '/']
        except:
            raise Exception('输入出错')
        else:
            return a, b ,c

    def get_result(self):
        d={'+':self.add,'-':self.sub,'*':self.mul,'/':self.div}
        print(d[self.c]())

    def add(self):
        sum=self.a+self.b
        return sum

    def sub(self):
        sum = self.a - self.b
        return sum
    def mul(self):
        sum = self.a * self.b
        return sum
    def div(self):
        try:
            sum = self.a / self.b
        except ZeroDivisionError:
            print('分母不能为0')
        else:
            return sum


if __name__=='__main__':
    c = C()
    c.get_result()
