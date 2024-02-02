import csv
f=open('../../快速上手配套资料/9.源代码/exampleWithHeader.csv','r')
reader=csv.DictReader(f)
for row in reader:
    print(row['Timestamp'],row['Fruit'],row['Quantity'])