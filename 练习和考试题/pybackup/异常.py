# 异常处理的保留住和逻辑

try:
    num = eval(input())
    print(num**2, end="")
except NameError:
    print("输入的不是整数")
except:
    print("遇见其他错误")
else:
    print("\r" + "结果:" + "{}".format(num**2))
finally:
    print("结束")
