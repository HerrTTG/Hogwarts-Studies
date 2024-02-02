import requests

url='https://q.ip5.me/'
try:
    r=requests.get(url+'?s=112.4.135.19',timeout=5)
    print(r.request.url)
    r.raise_for_status()
except:
    print('爬取失败',f'{r.status_code}',end='\n')
    print(r.request.url)
else:
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
