from multiprocessing import Process
import os,time



def test():
    print(f'我是子进程{os.getpid()},我的父进程是{os.getppid()}')
    time.sleep(1)



if __name__=='__main__':
    print('主进程开始')
    mulls=[]
    for i in range(5):
        #创建进程5个
        pro=Process(target=test)
        #pro.join()#阻塞主进程，使用此方法后，主进程必须等待子进程完成才执行下一段代码。
        # 并且子进程根据for循环一个一个进行执行，多线程变单线程！
        #解决办法 写到ls里
        mulls.append(pro)
        pro.start()

    #此时列表中的每个对象都是一个子进程
    #同时父进程循环遍历每个对象
    #调用join来判断是否执行完成，没完成就等待，完成就跳过。但和前面写法不一样的是，此时所有创建的线程已经start了，只需等待所有线程完成。
    #而不是等到一个线程完成后再去start下一个子线程
    for i in mulls:
         i.join()
    print('主进程结束')#主进程其实是所有子进程结束后才结束，但不代表主进程不可以提前执行自己的代码


