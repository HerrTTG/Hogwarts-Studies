class Login():
    def login(self, method, url, kwargs) -> object:
        """
        登录接口的实现
        request为request方法的对象
        """
        r = super().send(method, url, kwargs)
        return r
