ls = [0, 1]
def fib():
    x=0
    y=1
    #0 1 1 2 3 5..
    def inner():
        nonlocal x,y
        sum=x+y
        ls.append(sum)
        x=y
        y=sum
    return inner

a=fib()
for i in range(5):
    a()
print(ls)