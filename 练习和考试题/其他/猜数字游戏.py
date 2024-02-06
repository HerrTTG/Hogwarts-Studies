import random

g=0
def guess(num,n):
        global g
        if num>n:
            print('太遗憾了，猜大了')
            g+=1
        elif num<n :
            print('太遗憾了，猜小了')
            g+=1
        elif num==n:
            g+=1
            print("猜了{}次，你猜中了！".format(g))
            return False

def numin():
    e=0
    while e<3:        
        try:
            num=eval(input('请输入0~100之间的一个整数:'))
            d=num**2
        except NameError:
            e+=1
            if e==3:
                print('输出错误多次，程序退出!')
            else:
                print('输出错误!')
            continue
        else:
            return num
        

def main():
    n=random.randint(0,100)    

    while True:
        if guess(numin(),n) ==False:
            break


main()

