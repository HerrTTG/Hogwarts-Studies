fo = open("D:\\Python\\练习和考试题\\文本处理\\正序.csv", 'r')

ls=[]

for line in fo:
    line=line.replace("\n","")
    line=line.replace(" ","")
    line=line.split(",")
    ls.append(";".join(line))

ls=ls[::-1]

for i in ls:
    i=i[::-1]
    print(i)