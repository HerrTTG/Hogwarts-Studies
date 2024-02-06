import wordcloud
import jieba

txt=open("D:\\Python\\练习和考试题\\文本处理\\《三国演义》[明]罗贯中.txt","r",encoding="utf-8").read()



word=jieba.lcut(txt)
d=dict()

for i in word:
    if len(i)<2:
        continue
    else:
        d[i]=d.get(i,0)+1


ls=list(d.items())

ls.sort(key= lambda x:x[1],reverse=True)

word=list()
for i in ls[0:10]:
    word.append(i[0])

s=''
for ch in word:
    s=s+ch+' '

w = wordcloud.WordCloud(
    width=1000, height=700, background_color="white", font_path="msyh.ttc"
)
w.generate(s)
w.to_file("D:\\Python\\练习和考试题\\文本处理\\三国演义.png")


