# 生成器推导式只是把列表推导式的外框[]换成()即可，
# 另外如果生成式推导式是函数调用的唯一参数，如fun(生成器推导式)则无需再使用()
a = ('a', 'b', 'c')
b = (1, 2, 3)

for i in (f'{i} {j}' for i in a for j in b):
    print(i)


def gen(text, iter):
    print(f'{text * next(iter)}')


My_iter = (i for i in range(1, 10))
gen("test", My_iter)
gen("test", My_iter)
