import logging
from frame.apis.login import Login


class LoginAuth(Login):
    """
    登录鉴权类，继承login接口的login方法。
    """

    def send(self, be, method, url, **kwargs):
        """
        Mix-in BaseAPI 的send方法。
        因为LoginAuth在接口类继承时在BaseAPI的左边，所以接口调用send方法实际执行的是loginAuth的send方法。

        在此send方法中，对请求参数进行拦截。
        并且调用登录鉴权方法,获取鉴权信息。

        返回拼装鉴权信息后的final_kwargs
        最后在调用父类的send方法，即BaseAPI的send完成发送请求。

        be:接口的类型名称 如department、customermegement
        method：请求方法
        url:请求地址
        **kwargs:不定长参数。包括request方法url后所有关键字参数

        """
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
        # 先判断self是否存在final_token属性，如果存在，就不在发送登录鉴权信息。
        # 减少重复获取token的不必要操作
        if hasattr(self, 'final_token') is False:
            logging.info('获取登录请求的鉴权信息.......')
            params = {'corpid': self.envinfo[be]['corpid'], 'corpsecret': self.envinfo[be]['SECRET']}
            #login方法继承自Login类，属于基础登录接口。
            r = self.login(self.request, 'GET', self.baseurl + '/cgi-bin/gettoken', params)
            try:
                assert r.json()['access_token']
            except AssertionError:
                logging.error('获取登录请求的鉴权信息失败')
                raise AssertionError
            else:
                self.final_token = {'access_token': r.json()['access_token']}
                logging.debug(f'请求的鉴权信息:{self.final_token}')

        # 拼装参数，由于token需要带入到URL参数中去，所以先判断是否存在params。
        #如果不存在，则直接赋值，否则更新
        if request_kwargs.get("params"):
            request_kwargs['params'].update(self.final_token)
        else:
            request_kwargs['params'] = self.final_token

        return request_kwargs
