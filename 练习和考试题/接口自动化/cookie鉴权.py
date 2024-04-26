import requests


class TestCookieVerfy:
    def setup_class(self):
        self.proxy = {"http": "127.0.0.1:8888", "https": "127.0.0.1:8888"}

    """
    有确认的cookie信息时 可以直接用cookies传递cookie
    """

    def test_cookie(self):
        r = requests.request("GET", "https://httpbin.ceshiren.com/cookies", verify=False, cookies={"tester": "hzy"})
        print(r.json())

    def test_cookie_request(self):
        # 1.获取cookie
        # 2.set cookie
        # 3.再次获取cookie，查看是否成功
        # 结果是request并不会自动保存第二次获取到的cookie 第三次访问的cookie信息还是为空

        r1 = requests.request("GET", "https://httpbin.ceshiren.com/cookies", verify=False)
        print(r1.json())

        r2 = requests.request("GET", "https://httpbin.ceshiren.com/cookies/set/tester123/aasssdd", verify=False)
        print(r2.json())

        r3 = requests.request("GET", "https://httpbin.ceshiren.com/cookies", verify=False)
        print(r3.json())

    def test_cookie_session(self):
        # 创建对象（重要）
        req = requests.session()

        # 对象发送请求
        # 此对象set的cookie 获取到cookie信息响应后。在下一次发送请求时，可以看到自动会携带上cookie
        r2 = req.request("GET", "https://httpbin.ceshiren.com/cookies/set/tester123/aasssdd", verify=False)
        print(r2.json())

        r3 = req.request("GET", "https://httpbin.ceshiren.com/cookies", verify=False)
        print(r3.json)
