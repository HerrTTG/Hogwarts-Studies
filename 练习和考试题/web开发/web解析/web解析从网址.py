import requests,bs4
res=requests.get('https://map.baidu.com/search/')
res.raise_for_status()
s4=bs4.BeautifulSoup(res.text,'html.parser')
#print(s4)
elems=s4.select('#search-button')
#CSS选择器



print(elems[0].attrs)
