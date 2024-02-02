import pyinputplus as pi
def bao():
    x=0
    y=0
    def cal(x1,y1):
        nonlocal x,y
        #nonlocal 表示内部函数将会修改外部函数的局部变量，从而实现存储内部函数的运算结果到外部变量中去。
        #这种带记忆存储功能的闭包函数适合写在一些需要保护的变量上。如游戏中角色移动的坐标参数等。根据实时的保留用户操作后的坐标。
        x+=x1
        y+=y1
        return print(f"现在x={x},y={y}")
    return cal

diaoyong=bao()

while True:
    n=pi.inputInt('输入n:')
    m=pi.inputInt('输入m:')
    diaoyong(n,m)

