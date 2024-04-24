import requests

# 代理的作用主要是方便抓包工具抓包。charles和fiddler都是讲自己设置为系统级代理端转发所有发出和接受的信息。
# 在request中设置本机地址为代理，就是将消息发给代理端，即抓包工具。又抓包工具进行转发和接受响应信息。
# 要注意本机的端口号要和charles中代理设置的监听端口号保持一致，fiddler暂时未发现影响。最好保持一致
proxies = {"http": 'http://127.0.0.1:8888', "https": 'http://127.0.0.1:8888'}

r = requests.request('POST', url='https://httpbin.testing-studio.com/post', proxies=proxies, verify=False)

print(r.text)
