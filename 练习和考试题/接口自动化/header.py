import requests

url = "https://httpbin.ceshiren.com/get"

params = {"status": "available"}
headers = {"User-Agent": "test123"}

response = requests.request("GET", url, params=params, headers=headers)
response.raise_for_status()

print('args:%s,User-Agent:%s ' % (response.json()['args'], response.json()['headers']['User-Agent']))
