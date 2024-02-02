import requests
res=requests.get('https://map.baidu.com/search/')
res.raise_for_status()
downloadfile=open('D:\\Python\\练习和考试题\\web开发\\web爬取\\爬取页面测试.txt','wb')
for i in res.iter_content(100000):
	downloadfile.write(i)
downloadfile.close()