import bs4,requests

url='https://www.python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text

soup=bs4.BeautifulSoup(demo,'html.parser')
#print(soup.prettify())
print(soup.title)

tag=soup.a

print(tag)#<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a>#
print(soup.a.name)#a
print(soup.a.parent.name)#p
print(soup.a.parent.parent.name)#body
print(tag.attrs)#{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
print(tag.attrs['href'])
print(tag.string)#Basic Python



newsoup=bs4.BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>",'html.parser')

print(newsoup.b.string)
print(type(newsoup.b.string))#<class 'bs4.element.Comment'>

