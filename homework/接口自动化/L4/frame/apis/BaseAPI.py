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
        发送前调用登录鉴权方法,获取鉴权信息。
        返回拼装鉴权信息后的**final_kwargs
        be:接口的类型名称 如department、customermegement
        method：请求方法
        url:请求地址
        **kwargs:不定长参数。包括request方法url后所有关键字参数
        """
        # 打包后的kwargs传入__login_auth方法
        final_kwargs = self.__login_auth(be, kwargs)

        #解包final_kwargs传入request方法
        r = self.request(method, url, **final_kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def __login_auth(self, be, request_kwargs):
        """
        登录鉴权方法
        根据环境信息选择登录的url和登录信息
        将登陆鉴权信息更新进request_kwargs中返回
        be:接口的类型名称 如department、customermegement
        request_kwargs:不定长参数的打包（字典形式）。包括request方法url后所有关键字参数。
        """
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
