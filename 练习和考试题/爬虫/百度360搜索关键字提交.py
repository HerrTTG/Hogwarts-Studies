import requests

#http://www.baidu.com/s?wd=keyword
#http://www.so.com/s?q=keyword

url='http://www.baidu.com/s'
kv={'wd':'Python'}
hd={'User-Agent':'Mozilla 5.0'}

try:
    r=requests.get(url,params=kv,headers=hd)
    #params 参数来补充url后的内容。来补充搜索关键字
    print(r.request.url)
    #r.request.url 表示爬虫请求的url是什么
    r.raise_for_status()
except:
    print('爬取失败')
    print(r.status_code)
else:
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
