
def dataread():
    fr = open("D:\\Python\\练习和考试题\\文本处理\\price2016.csv", "r",encoding='utf-8')
    ls = []
    for line in fr:
        line = line.replace("\n","")
        ls.append(line.split(","))
    fr.close()
    return ls
    #读取CSV转化为二维列表


def fill_data(locls):
    seg4 = '<tr><td align="center">{}</td><td align="center">\
        {}</td><td align="center">{}</td><td align="center">{}</td></tr>\n'.format(*locls)
    #每一行的所有元素依次写入槽内
    return seg4


def main():
    ls=[]
    ls=dataread()
    fw = open("D:\\Python\\练习和考试题\\文本处理\\price2016.html", "w")
    fw.write(seg1)

    fw.write('<th width="25%">{}</th>\n<th width="25%">\
         {}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n'.format(*ls[0])) 
    #seg2 
    # format(*ls[0]) 意思是将第一行的所有元素依次按照序列顺序从第一个展示到对应的槽内
    fw.write(seg3)
    for i in range(len(ls)-1):
        #len(ls)-1是因为表头已经排除在外了，需要遍历的是从ls[1]开始到最后的，所以次数-1
        fw.write(fill_data(ls[i+1]))
        #ls[i+1]就是从0+1即第二行元素开始
    fw.write(seg5)
    fw.close()



seg1 = '''
<!DOCTYPE HTML>\n<html>\n<body>\n<meta charset=gb2312>
<h2 align=center>2016年7月部分大中城市新建住宅价格指数</h2>
<table border='1' align="center" width=70%>
<tr bgcolor='orange'>\n'''
seg3 = "</tr>\n"
seg5 = "</table>\n</body>\n</html>"
main()