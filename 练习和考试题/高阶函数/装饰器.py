import time
import functools


def caltime(func):
    @functools.wraps(func)
    #装饰装饰器的装饰器用于解决func.__name__会被污染的问题
    def callfunc():
        print('函数开始执行')
        starttime = time.time()
        func()
        #内层函数可以直接继承闭包的局部域的参数即func
        endtime=time.time()
        print('函数结束执行')
        print(f'总共耗时{(endtime-starttime):.2f}')
    return callfunc

#装饰器特有的写法实现了运行main()函数的调用的同时都调用一个caltime(main)
#实现在不修改原功能代码的基础上将部分新增的功能附加上去
#如本案例中，main函数表示原有功能，装饰器caltime实现了计算main函数执行时间并且打印额外的内容的功能
#而且装饰器可方便于复用到其他任何功能的函数调用上，从而减少代码冗余
#如果有多个糖，执行顺序由下至上
#@caltime是一个语法糖，等价于 main=caltime(main)
#@functools.wraps的作用是一个高阶函数 用来装饰装饰器,否则main.__name__将返回callfunc 而不是main

@caltime
def myfunc():
    time.sleep(2)
    print('我是需要执行的函数')


myfunc()
print(myfunc.__name__)



