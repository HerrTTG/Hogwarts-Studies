zhongwen = "零一二三四五六七八九"

shuru = input()

for a in shuru:
    # a循环赋值等价shuru中的字符
    print(zhongwen[eval(a)], end="")
    # 增加end=""参数表示输出后不增加换行。a因为循环，其实是一个一个a带入进来运算输出的。
