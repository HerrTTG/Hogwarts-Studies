import requests

data = {'tester': "haizhenyu"}

r = requests.post("https://httpbin.ceshiren.com/post",
                  data=data, verify=False)

rj = requests.post("https://httpbin.ceshiren.com/post",
                   json=data, verify=False)

print(r.text)
