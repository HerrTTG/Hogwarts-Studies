class LoginAuth():
    def login(self, request, method, url, params):
        """
        登录接口的实现
        request为request方法的对象
        """
        r = request(method, url, params=params, verify=False)
        return r
