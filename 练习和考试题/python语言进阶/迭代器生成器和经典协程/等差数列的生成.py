def arp(begin, step, end=None):
    result = type(begin + end)(begin)  # 用type获取begin+end的结果的类型，如int+float的结果是folat。然后再将begin强制转换为该类型
    forever = end is None  # 判断end是否为空，为空则表示生成无穷数列
    index = 0  # 索引值，根据生成器的每次调用不断累加
    while forever or result < end:  # 当无穷时，或者结果值小于结束值时，不断循环。
        yield result  # 返回结果
        index += 1  # 索引+1
        result = begin + step * index  # 并重新计算等差的结果。


print(list(arp(1, 0.5, 3)))
