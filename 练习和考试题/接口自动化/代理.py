import requests

proxies = {"http": 'http://127.0.0.1:8888', "https": 'http://127.0.0.1:8888'}

r = requests.request('POST', url='https://httpbin.testing-studio.com/post', proxies=proxies, verify=False)
