import requests

url = 'https://httpbin.ceshiren.com/post'

data = {"key": "vaule"}

r = requests.request("POST", url, json=data, verify=False)

##verify=False 可以不校验证书，方便抓包

print(r.text)
