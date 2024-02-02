import time


def canshu(msg):
    def caltime(func):
        def callfunc():
            print('函数开始执行')
            starttime = time.time()
            func()
            endtime=time.time()
            print('函数结束执行')
            print(f'[{msg}]总共耗时{(endtime-starttime):.2f}')
        return callfunc()
    return caltime
#装饰器传参，简单的概括就是在装饰器外在套一个闭包，利用闭包的变量域可继承性，将参数传递下去。
@canshu(msg='mainA')
def main():
    time.sleep(2)
    print('我是需要执行的函数')

main()



