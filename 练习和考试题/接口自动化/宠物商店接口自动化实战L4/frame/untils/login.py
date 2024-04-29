import logging
import requests


class Loginrequest():
    def __init__(self):
        self.r = requests.request
    def login(self, url, userdate):
        res = self.r('POST', url, json=userdate, verify=False)
        logging.info(f'登录接口返回信息：{res.text}')
        try:
            assert res.status_code == 200
            assert res.json()["data"]["token"]
        except AssertionError:
            logging.debug(f'登录失败')
            raise AssertionError
        else:
            return res.json()

    def role_login(self, url, role, envinfo):

        res = self.login(url, envinfo[role]['userinfor'])
        return res["data"]["token"]
