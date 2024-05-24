import jieba

fo = open("E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\文本处理\沉默的羔羊.txt", "r", encoding='utf-8')
txt=fo.read()
for ch in "!\"#$%&()*+-,./:;<=>?@[\\]^_{|}'`~":
        txt = txt.replace(ch, "")
ls=jieba.lcut(txt)
#ls.remove("\n")
#print(ls)
d=dict()
for i in ls:
     if len(i)<2:
           continue
     else:
           d[i]=d.get(i,0)+1
     
lt=list(d.items())

lt.sort(key= lambda x:x[1],reverse=True)

print(lt[0][0])

