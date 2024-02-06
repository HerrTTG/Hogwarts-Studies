
s=input()
try:
    ##complex(s)==complex(eval(s))比较可以排除非数。包括8进制和16进制
    if complex(s)==complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")