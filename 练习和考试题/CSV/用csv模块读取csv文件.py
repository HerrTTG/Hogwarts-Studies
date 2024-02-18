import csv

f = open('E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\CSV\output.csv', 'r')
fr=csv.reader(f)
#print(list(fr))

for row in fr:
    print('Row #' + str(fr.line_num) + str(row))
    #line_num代表行数的标识符，再循环中从1到结尾

