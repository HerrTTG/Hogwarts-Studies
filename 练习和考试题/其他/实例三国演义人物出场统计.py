import jieba

txt = open("D:\\Python\\练习和考试题\\文本处理\\《三国演义》[明]罗贯中.txt", "r", encoding="utf-8").read()
excludes = {
    "将军",
    "却说",
    "二人",
    "荆州",
    "不能",
    "如此",
    "不可",
    "商议",
    "如何",
    "军士",
    "左右",
    "引兵",
    "军马",
    "次日",
    "大喜",
    "主公",
    "天下",
    "东吴",
    "于是",
    "今日",
    "不敢",
    "陛下",
    "人马",
    "都督",
    "魏兵",
}
# 排除非人名
words = jieba.lcut(txt)
counts = {}

for i in words:
    if len(i) == 1:
        continue
    elif i == "孔明" or i == "孔明曰" or i == "诸葛亮" or i == "诸葛孔明":
        rword = "诸葛亮"
    elif i == "曹操" or i == "曹孟德" or i == "曹孟德" or i == "孟德曰" or i == "丞相":
        rword = "曹操"
    elif i == "玄德" or i == "刘玄德" or i == "玄德曰" or i == "刘备":
        rword = "刘备"
    elif i == "关公" or i == "关云长" or i == "关羽" or i == "云长":
        rword = "关羽"
    else:
        rword = i
    counts[rword] = counts.get(rword, 0) + 1
    # 判断一个字的跳出循环不计入字典，如“是”
    # 判断别称，规范到一个人名上进行统计

for i in excludes:
    del counts[i]
    # 排除非人名结果

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))
