import bs4

f=open('D:\\Python\\练习和考试题\\web开发\\web解析\\example.html','r')
s4=bs4.BeautifulSoup(f,'html.parser')
elems=s4.select('#author')
print(elems)