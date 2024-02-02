import requests
url='https://item.jd.com/10068218195642.html'
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print(r.status_code)
    print('爬取失败')