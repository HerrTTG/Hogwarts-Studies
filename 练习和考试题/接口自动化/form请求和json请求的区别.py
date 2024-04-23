import requests

data = {'tester': "haizhenyu"}
headers = {"Content-Type": "application/json"}

r = requests.post("https://httpbin.ceshiren.com/post",
                  data=data, verify=False)

rj = requests.post("https://httpbin.ceshiren.com/post",
                   json=data, verify=False)

rjj = requests.post("https://httpbin.ceshiren.com/post",
                    data=data, headers=headers, verify=False)

print(r.json()['headers']["Content-Type"])
print(rj.json()['headers']["Content-Type"])
print(rjj.json()['headers']["Content-Type"])
