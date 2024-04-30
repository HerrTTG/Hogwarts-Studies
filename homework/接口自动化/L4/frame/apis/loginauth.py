class LoginAuth():
    def login(self, request, method, url, params):
        r = request(method, url, params=params, verify=False)
        return r
