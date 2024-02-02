#GovRptWordCloudv2.py
import jieba
import wordcloud
from imageio import imread
mask = imread("D:\\Python\\练习和考试题\\实例词云\\bitlogo.png")
excludes = ['联网']
count={}
f = open("D:\\Python\\练习和考试题\\实例词云\\关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)

for i in ls:
    if len(i) <2 :
        continue
    elif i in excludes:
        continue
    else:
        count[i]=count.get(i,0)+1

maxw=list(count.items())

maxw.sort(key=lambda x:x[1],reverse=True)
ls_new=[]
for i in maxw[0:100]:
    ls_new.append(i[0])
#排序 并且只取前100的词进行展示

txt = " ".join(ls_new)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("D:\\Python\\练习和考试题\\实例词云\\grwordcloudm.png")


