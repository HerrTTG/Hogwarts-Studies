import bs4,requests

url='https://www.python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text

soup=bs4.BeautifulSoup(demo,'html.parser')



for link in soup.find_all('a'):
    print(link.get('href'))