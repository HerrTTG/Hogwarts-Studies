import json
import requests

from until.log import logger


class Service():

    def __init__(self):
        self.request = requests.request

    def request_analysis(self, mothod: str, request_kwargs: dict):
        """
        解析字典解析发送方式，url,和参数。
        并检查是否有final_token需要进行拼装到参数中。
        调用send方法发出
        """
        # 拼装参数，由于token需要带入到URL参数中去，所以先判断是否存在params。
        # 如果不存在，则直接赋值，否则更新

        logger.info('run request_analysis')
        logger.info(mothod, request_kwargs)

        send_url = request_kwargs.pop('url')
        finnaly_kwargs = request_kwargs

        if finnaly_kwargs.get('params') and hasattr(self, 'final_token'):
            finnaly_kwargs['params'].update(self.final_token)
        elif hasattr(self, 'final_token'):
            finnaly_kwargs['params'] = self.final_token

        return self.send(mothod, send_url, finnaly_kwargs)


    def login_auth(self, step: dict):
        """
        获取登录鉴权，并赋予赋值给final_token
        """
        if hasattr(self, 'final_token') is False:
            logger.info('获取登录请求的鉴权信息.......')
            kwargs = {'params': step['auth']['params']}
            # login方法继承自Login类，属于基础登录接口。
            r = self.send('GET', step['auth']['url'], kwargs)
            try:
                assert r.json()['access_token']
            except AssertionError:
                logger.error('获取登录请求的鉴权信息失败')
                raise AssertionError
            else:
                self.final_token = {'access_token': r.json()['access_token']}
                logger.debug(f'请求的鉴权信息:{self.final_token}')


    def send(self, method, url, kwargs: dict) -> object:
        """
        """
        # 解包kwargs传入request方法发送请求
        r = self.request(method, url, **kwargs, verify=False)
        logger.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r
