'''
作业要求
编写一个Python程序，实现一个计数器函数，该函数能够记录特定函数的调用次数。你需要使用闭包和装饰器来实现这个功能。
'''



def count_call(func):
    count=0
    def countsum(*args):
        nonlocal count
        count+=1
        print(f'执行第{count}次')
        return func(*args)
    return countsum


@count_call
def testfunc(i):
    print(str(i)+'0')

if __name__=='__main__':
    for i in range(1,11):
        testfunc(i)
