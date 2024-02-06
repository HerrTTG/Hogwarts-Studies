fo=open("D:\\Python\\练习和考试题\\文本处理\\正序.csv",'r')



for line in fo:
    line=line.replace("\n",'')
    t=line.split(",")
    t=t[::-1]
    print(",".join(t))