import requests


class Loginrequest():
    def __init__(self, authname, url):
        self.r = requests.request
        self.authname = authname
        self.url = url

    def login(self, url, userdate):
        return self.r('POST', url, json=userdate, verify=False)

    def get_token(self):
        if self.authname == 'admin':
            user_data = {"username": "admin123", "password": "admin123", "code": ""}
            res = self.login(self.url + "/admin/auth/login", user_data)
            return res.json()["data"]["token"]
        elif self.authname == 'wx':
            client_data = {"username": "user123", "password": "user123"}
            res = self.login(self.url + "/wx/auth/login", client_data)
            return res.json()["data"]["token"]
