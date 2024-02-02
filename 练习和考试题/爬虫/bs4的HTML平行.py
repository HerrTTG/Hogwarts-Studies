import bs4,requests

url='https://www.python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text

soup=bs4.BeautifulSoup(demo,'html.parser')

#平行
print(soup.a.next_sibling) #a的下一个平行是一个字符串标签
#<a class=...</a> and <a class=...</a>
print(soup.a.next_sibling.next_sibling)#再下一标签才是第二个a标签

print(soup.a.previous_sibling)#第一个a标签的再前一个标签也是一个字符串标签
print(soup.a.previous_sibling.previous_sibling)#none 没有了

print('--------------------------------------')
for sibiling in soup.a.next_siblings:
    print(sibiling)


for sibiling in soup.a.previous_siblings:
    print(sibiling)