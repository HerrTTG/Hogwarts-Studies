import csv

f=open('./写入csvtest.csv','w',newline='')
outputwriter=csv.writer(f,delimiter='|',lineterminator='\n\n')
outputwriter.writerow(['spam','eggs','bacon','ham'])

outputwriter.writerows([['Hello','world','eggs','bacon','ham'],[1,2,3,4,5]])
f.close()