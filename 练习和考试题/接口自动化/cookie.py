import requests

# 第一种传递cookie的方法 直接写入header中传入

# header={'User-Agent': 'tester/haizhenyu', 'Accept-Encoding': 'gzip, deflate',
#         'Accept': '*/*', 'Connection': 'keep-alive', 'Cookie': 'howarts=school'}
# r=requests.request('GET',url='https://httpbin.testing-studio.com/cookies',headers=header,verify=False)
#
#
# print(r.request.headers)


# 第二种方法 直接使用cookie参数传入
# 可以一次传入多个cookie
cookie = {'cookies_are': 'howarts', 'techer': 'AD'}
r = requests.request('GET', url='https://httpbin.testing-studio.com/cookies', cookies=cookie, verify=False)
print(r.request.headers)
