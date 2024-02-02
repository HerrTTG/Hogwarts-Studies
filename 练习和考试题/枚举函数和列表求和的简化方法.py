import  pyinputplus
# 测试枚举函数的用法
# 测试自定义输入验证的方法inputCutomer
# 设置一个校验函数 sum10
# 将函数名带入inputCustom（）

#简化办法 枚举函数enumerate 简化获取list的索引和值的过程
#nlist[i]=int(digit) 然后将列表中的字符串信息转化为int整数
#sum（list）sum一个全为整数的列表,可省略for循环遍历的过程
#raise Exception('Wrong')抛出异常


def sum10(n):
    nlist=list(n)
    for i ,digit in enumerate(nlist):
        nlist[i]=int(digit)
    if sum(nlist)!=10:
        raise Exception('Wrong')
    else:
        return int(n)
res=pyinputplus.inputCustom(sum10)