import json
import logging
import requests
## base url :https://qyapi.weixin.qq.com
from frame.apis.loginauth import LoginAuth


class BaseAPI(LoginAuth):
    def __init__(self, envinfo):
        """
        实例化环境信息，从环境信息中获取baseurl
        生成request方法的对象
        """
        self.envinfo = envinfo
        self.baseurl = self.envinfo['url']
        self.request = requests.request

    def send(self, be, method, url, **kwargs):
        """
        接口发送请求
        """
        final_kwargs = self.__login_auth(be, kwargs)
        r = self.request(method, url, **final_kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def __login_auth(self, be, request_kwargs):
        if hasattr(self, 'final_token') is False:
            logging.info('获取登录请求的鉴权信息.......')
            params = {'corpid': self.envinfo[be]['corpid'], 'corpsecret': self.envinfo[be]['SECRET']}
            r = self.login(self.request, 'GET', self.baseurl + '/cgi-bin/gettoken', params)
            try:
                assert r.json()['access_token']
            except AssertionError:
                logging.error('获取登录请求的鉴权信息失败')
                raise AssertionError
            else:
                self.final_token = {'access_token': r.json()['access_token']}
                logging.debug(f'请求的鉴权信息:{self.final_token}')


        if request_kwargs.get("params"):
            request_kwargs['params'].update(self.final_token)
        else:
            request_kwargs['params'] = self.final_token

        return request_kwargs
