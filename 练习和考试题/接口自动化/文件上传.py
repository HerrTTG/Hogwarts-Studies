import requests

url = 'https://httpbin.ceshiren.com/post'

# r=requests.request("POST",url,files={"hogwarts_file":open("./123test.txt","rb")},verify=False)

# value 用元组传递可以指定文件名
r = requests.request("POST", url,
                     files={"hogwarts_file": ("changename.text", open("./123test.txt", "rb"))}, verify=False)

##verify=False 可以不校验证书，方便抓包

print(r.text)
