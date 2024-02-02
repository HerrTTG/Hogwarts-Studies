fo=open("/练习和考试题/文本处理/test.csv", "r")

ls=[]

for line in fo:
    line=line.replace("\n",'')
    ls=line.split(",")
    #将一行的内容去掉逗号变成一个列表['GROUP_CODE', 'GROUP_NAME', 'PRI_IDENTITY', 'EFF_DATE', 'EXP_DATE']
    #print(ls)
    lns=""
    for s in ls:
        lns+=s+"\t"
    #从列表中将元素取出，然后累加成一个新的长行字符串，每个元素后追加一个\t来隔开 方便展示
    print(lns)
fo.close()