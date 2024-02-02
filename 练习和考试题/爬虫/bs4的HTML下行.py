import bs4,requests

url='https://www.python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text

soup=bs4.BeautifulSoup(demo,'html.parser')

#下行
print(soup.head)#<head><title>This is a python demo page</title></head>
print(soup.head.contents)#获取head标签下的子标签列表

print(soup.body)
'''<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body>'''
print(soup.body.contents)#/n 回车换行也是一个节点

for child in soup.body.children:
    print(child)

for child in soup.body.descendants:
    print(child)



