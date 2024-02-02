import csv
f=open('../../快速上手配套资料/9.源代码/example.csv','r')
fr=csv.reader(f)
#print(list(fr))

for row in fr:
    print('Row #' +str(fr.line_num)+' '+str(row) )
    #line_num代表行数的标识符，再循环中从1到结尾

