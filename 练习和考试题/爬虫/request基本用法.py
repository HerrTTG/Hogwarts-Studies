import requests

r=requests.head('https://www.baidu.com')
print(r.status_code)
r.encoding='utf-8'
print(r.headers)
