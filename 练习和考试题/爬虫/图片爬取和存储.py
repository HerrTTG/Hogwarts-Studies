import requests

url='https://www.natgeo.com.cn/pic/program_default.768.jpg'
path='./'+url.split('/')[-1]
try:
    r=requests.get(url)
    r.raise_for_status()
except:
    print('爬取失败')
    print(r.status_code)
else:
    with open(path,'wb') as f:
        f.write(r.content)
        #r.content 内容的二进制形式
        #图片是二进制保存的数据流
