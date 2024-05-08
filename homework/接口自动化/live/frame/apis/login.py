class Login():
    def login(self, method, url, kwargs) -> object:
        """
        登录接口的实现。
        只负责描述此接口所做的事。
        实际动作是对象其父类的send方法去实现，即BaseAPI的send方法。
        """
        r = super().send(method, url, kwargs)
        return r
