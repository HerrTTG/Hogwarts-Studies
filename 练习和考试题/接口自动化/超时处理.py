import requests


class TestReq:
    def test1(self):
        r = requests.get('http://github.com')

    def test_timeout(self):
        """
        用例设置超时，超时后自动失败。不影响后续用例的执行
        """
        r = requests.get('http://github.com', timeout=0.01)

    def test2(self):
        r = requests.get('http://github.com')
