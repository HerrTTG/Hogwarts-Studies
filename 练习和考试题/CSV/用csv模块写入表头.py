import csv
f=open('./output.csv','w',newline='')
writer=csv.DictWriter(f,['Name','Pet','Phone'])
#writer.writeheader()
#这里必须要用writerheader来写入表头，否则表头将被省略不出现在文件中
writer.writerow({'Name':'Alice','Pet':'cat','Phone':'555-1234'})
writer.writerow({'Name':'Bob','Phone':'555-9999'})
writer.writerow({'Phone':'555-1234','Name':'Carol','Pet':'dog'})
#字典中的顺序并不重要，值的位置，是早在writer对象创建时，由key的顺序确定的