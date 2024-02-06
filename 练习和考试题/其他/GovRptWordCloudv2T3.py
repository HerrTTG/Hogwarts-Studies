#GovRptWordCloudv2.py
import jieba
import wordcloud
from imageio import imread
mask = imread("D:\\Python\\练习和考试题\\实例词云\\bitlogo.png")
excludes = list()
f = open("D:\\Python\\练习和考试题\\实例词云\\新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
s=set(ls)
ls=list(s)

for i in ls:
    if len(i) <2 :
        ls.remove(i)
    #排除小于2的词
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("D:\\Python\\练习和考试题\\实例词云\\grwordcloudm.png")


