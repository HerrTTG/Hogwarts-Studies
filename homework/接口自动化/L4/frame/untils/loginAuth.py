import logging
from frame.apis.login import Login


class LoginAuth(Login):
    """
    登录鉴权类，继承login接口的login方法。
    Mix-in send 方法。
    在对象调用send方法时，先对参数进行处理。获取登录鉴权信息。并加入其中。
    最后在调用父类的send方法完成发送请求的实现。
    """

    def send(self, be, method, url, **kwargs):
        final_kwargs = self.__login_auth(be, kwargs)
        r = super().send(method, url, final_kwargs)
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
