import jieba

txt = open("D:\\Python\\练习和考试题\\文本处理\\《三国演义》[明]罗贯中.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}

for i in words:
    if len(i) == 1:
        continue
    else:
        counts[i] = counts.get(i, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))
