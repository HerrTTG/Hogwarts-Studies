#可能会返回503错误 就有可能是页面对head头做了限制
#可以用r.request.headers 来查看爬虫给页面发送的请求头
#'User-Agent': 'python-requests/2.31.0' 说明这是个爬虫脚本 就会被网页审查 导致503


import requests
url='https://www.amazon.cn/dp/B004VKTQFA?ref_=Oct_DLandingS_D_f8cf24a4_0&th=1'
kv={'User-Agent':'Mozilla 5.0'}
try:
    r=requests.get(url,headers=kv)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding

except:
    print(r.status_code)

else:
    print(r.text[1000:2000])

