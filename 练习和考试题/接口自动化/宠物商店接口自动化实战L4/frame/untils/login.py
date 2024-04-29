import logging
import requests


class Loginrequest():
    def __init__(self):
        self.r = requests.request

    def __login(self, url, userdate):
        res = self.r('POST', url, json=userdate, verify=False)
        logging.debug(f'登录接口返回信息：{res.text}')
        try:
            assert res.status_code == 200
            assert res.json()["data"]["token"]
        except AssertionError:
            logging.debug(f'登录失败')
            raise AssertionError
        else:
            return res.json()["data"]["token"]

    def role_login(self, url, user):
        res = self.__login(url, user)
        return res
