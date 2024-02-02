s = input()

try:
    d = eval(s)
    e = {}
    for k in d:
        e[d[k]] = k
    print(e)
except:
    print("输入错误")
