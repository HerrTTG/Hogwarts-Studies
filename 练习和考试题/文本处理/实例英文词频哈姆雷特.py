def getText():
    txt = open("D:\\Python\\练习和考试题\\文本处理\\hamlet.txt", "r").read()
    # 打开一个文件
    txt = txt.lower()
    # 全部转小写
    for ch in "!\"#$%&()*+-,./:;<=>?@[\\]^_{|}'`~":
        txt = txt.replace(ch, "")
    # 去除所有的特殊标点符号
    return txt


hamlet = getText()
words = hamlet.split()
# 分割空格 返回列表
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
# 通过字典来统计单词的出现频率
items = list(counts.items())
# count.item()返回全部的键值对为元组类型，list将所有元组组成一个列表[(a,b),(c,d)]
items.sort(key=lambda x: x[1], reverse=True)
# 排序

e=0
a=0
while e<10:
    while True:
        word, count = items[a]
        if len(word)<2:
            a+=1
            continue
        else:
            print("{0:<10}{1:>5}".format(word, count))
            e+=1
            a+=1
            break