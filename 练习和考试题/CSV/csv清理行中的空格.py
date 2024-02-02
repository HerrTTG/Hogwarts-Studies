fo=open("/练习和考试题/文本处理/正序.csv", 'r')

for line in fo:
    line=line.replace(" ","")
    print(line,end="")

"""也可用整读文件的方法s=fo.read()  s=s.replace(" ","")"""