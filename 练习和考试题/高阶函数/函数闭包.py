def power(exp):
    def cal(base):
        return print(base ** exp)
    return cal

squ=power(2)
#实现2次方
cube=power(3)
#实现3次方

#调用函数并传入计算的值
squ(5)
cube(5)
#利用闭包的特性，将一个简单的高阶函数描述成两个不同的功能 而无需修改更多的代码。
#这就是闭包的优势。
