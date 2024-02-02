import re

num=re.compile(r'(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d)+')

fo=open("C:\\Users\\96436\\Desktop\\123.txt","r").read()

mo=num.findall(fo)
for i in mo:
    print(i)

