# TempConvert.py
"""这是一段注释 
#只能进行单行注释
而我可以任意行"""

TempStr = input()
if TempStr[0] in ["F", "f"]:
    # 从后向前数第一个字符为F或者f
    C = (eval(TempStr[1:]) - 32) / 1.8
    # [1:]表示第2个字符开始到最后所有的字符
    print("C{:.2f}".format(C))
elif TempStr[0] in ["C", "c"]:
    F = 1.8 * eval(TempStr[1:]) + 32
    print("F{:.2f}".format(F))
else:
    print()  # 不输入任何错误提示
