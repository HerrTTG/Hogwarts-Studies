import requests

class Loginrequest():
    def __init__(self, authname, envinfo):
        self.r = requests.request
        self.authname = authname
        self.envinfo = envinfo
        self.url = envinfo['url']

    def login(self, url, userdate):
        return self.r('POST', url, json=userdate, verify=False)

    def get_token(self):
        if self.authname == 'admin':
            res = self.login(self.url + "/admin/auth/login", self.envinfo['admin']['userinfor'])
            return self.url, res.json()["data"]["token"]
        elif self.authname == 'wx':
            res = self.login(self.url + "/wx/auth/login", self.envinfo['wx']['userinfor'])
            return self.url, res.json()["data"]["token"]
