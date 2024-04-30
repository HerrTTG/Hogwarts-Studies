import json
import logging
import requests
## base url :https://qyapi.weixin.qq.com
from frame.apis.loginauth import LoginAuth


class BaseAPI(LoginAuth):
    def __init__(self, envinfo):
        self.envinfo = envinfo
        self.baseurl = self.envinfo['url']
        self.request = requests.request

    def send(self, be, method, url, **kwargs):
        final_kwargs = self.__login_auth(be, kwargs)
        r = self.request(method, url, **final_kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def __login_auth(self, be, request_kwargs):
        if hasattr(self, 'final_token') is False:
            params = {'corpid': self.envinfo[be]['corpid'], 'corpsecret': self.envinfo[be]['SECRET']}
            r = self.login(self.request, 'GET', self.baseurl + '/cgi-bin/gettoken', params)
            self.final_token = {'access_token': r.json()['access_token']}

        if request_kwargs.get("params"):
            request_kwargs['params'].update(self.final_token)
        else:
            request_kwargs['params'] = self.final_token

        return request_kwargs
