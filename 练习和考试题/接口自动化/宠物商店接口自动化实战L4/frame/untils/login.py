import requests

class Loginrequest():
    def __init__(self, authname, envinfo):
        self.r = requests.request
        self.authname = authname
        self.envinfo = envinfo

    def login(self, url, userdate):
        return self.r('POST', url, json=userdate, verify=False)

    def get_token(self):
        if self.authname == 'admin':
            url = self.envinfo['admin']['url']
            res = self.login(url + "/admin/auth/login", self.envinfo['admin']['userinfor'])
            return url, res.json()["data"]["token"]
        elif self.authname == 'wx':
            url = self.envinfo['wx']['url']
            res = self.login(url + "/wx/auth/login", self.envinfo['wx']['userinfor'])
            return url, res.json()["data"]["token"]
