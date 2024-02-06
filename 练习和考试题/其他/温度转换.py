# TempConvert.py
"""这是一段注释 
#只能进行单行注释
而我可以任意行"""
TempStr = input("Please input Temp includ symbol(10C):")
if TempStr[-1] in ["F", "f"]:
    # 从后向前数第一个字符为F或者f
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("Convert temp to C:{:.2f}C".format(C))
elif TempStr[-1] in ["C", "c"]:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("Convert temp to F:{:.2f}F".format(F))
else:
    print("Input format wrong!")
