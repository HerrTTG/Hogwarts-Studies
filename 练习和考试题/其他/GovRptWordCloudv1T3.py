#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("D:\\Python\\练习和考试题\\实例词云\\新时代中国特色社会主义.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", max_words = 15
    )#设置最大输出字为15次，但是要注意这里的15
w.generate(txt)
w.to_file("D:\\Python\\练习和考试题\\实例词云\\grwordcloud.png")


