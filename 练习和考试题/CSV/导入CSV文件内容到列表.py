fo=open("/练习和考试题/文本处理/test.csv", "r")

ls=[]

for line in fo:
    line=line.replace("\n","")
    #print(line)
    ls.append(line.split(","))
    #line.split(",")生成的是一个列表将字符串'GROUP_CODE,GROUP_NAME,PRI_IDENTITY,EFF_DATE,EXP_DATE'按照逗号分隔生成为一个列表
    #即生成['GROUP_CODE', 'GROUP_NAME', 'PRI_IDENTITY', 'EFF_DATE', 'EXP_DATE']
    #然后再将这个列表加入到ls这个大列表中，变为二维列表
print(ls)
fo.close()
