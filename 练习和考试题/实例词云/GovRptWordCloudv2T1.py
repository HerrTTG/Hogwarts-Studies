#GovRptWordCloudv2.py
import jieba
import wordcloud
from imageio import imread
mask = imread("D:\\Python\\练习和考试题\\实例词云\\fivestart.png")
#mask根据某一张图片的形状绘制词云
excludes = { }
f = open("D:\\Python\\练习和考试题\\实例词云\\新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )#mask根据某一张图片的形状绘制词云
w.generate(txt)
w.to_file("D:\\Python\\练习和考试题\\实例词云\\grwordcloudm.png")


