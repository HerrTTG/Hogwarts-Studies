import bs4,requests

url='https://www.python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text

soup=bs4.BeautifulSoup(demo,'html.parser')

#上行
print(soup.title.parent)#<head><title>This is a python demo page</title></head
#soup.html.parent就是他本身 就是全部的html信息

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
#p
#body
#html
#[document]