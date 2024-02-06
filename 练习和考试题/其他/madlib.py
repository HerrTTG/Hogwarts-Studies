import  re,pyinputplus
f=open('D:\\Python\\练习和考试题\\文本处理\\madlibs.txt','r+',encoding="utf-8")
txt=f.read()

#用正则表达式来描述需要替换的内容
ch=re.compile(r'ADJECTIVE|NOUN|A*D*VERB')

ls=ch.findall(txt)
#找出来形成列表
d={}
for i in ls:
    print('Enter an '+i)
    #询问替换成什么内容
    d[i]=pyinputplus.inputStr()
    #将输入的替换值和原本的值形成一个字典，key为原文，value为替换值

for i in range(len(d)):
    k,v= d.popitem()
    #随机取出一个k和v
    if k=='ADVERB' or k=='VERB':
        k='A*D*VERB'
        #由于ADVERB和VERB是一个正则生成2种结果，在这里需要归一成原始的正则表达式。否则将会出现AD123这种结果，
        # 即ADVERB后面的VERB被替换，但不是ADVERB这个整体被替换
    txt=re.sub(k,v,txt)
    #对文本字符流进行替换

f.seek(0)
#指针归位开头
f.write(txt)
#写文档
f.close()
