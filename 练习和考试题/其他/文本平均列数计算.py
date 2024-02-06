fo=open("D:\\Python\\练习和考试题\\文本处理\\latex.log","r")

suml=0
sumc=0
for line in fo:
    line=line.replace("\n","")
    if len(line)==0:
        continue
    else:
       suml+=1
       sumc+=len(line)

print("{}".format(round(sumc/suml)))
