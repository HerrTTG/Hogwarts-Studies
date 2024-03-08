import requests

url = "https://httpbin.ceshiren.com/post"
params = {
    "post_key": "post_value"
}
# 发出 POST 请求，r 接收接口响应
r = requests.post(url, json=params)

print(r.text)
