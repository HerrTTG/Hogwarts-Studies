import bs4,requests

url='https://www.python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text

soup=bs4.BeautifulSoup(demo,'html.parser')

print(soup.prettify())

print(soup.a.prettify())