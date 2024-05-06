import json
import logging
import requests
## base url :https://qyapi.weixin.qq.com


class BaseAPI():
    def __init__(self, envinfo):
        """
        实例化环境信息，从环境信息中获取baseurl
        生成request方法的对象
        """
        self.envinfo = envinfo
        self.baseurl = self.envinfo['url']
        self.request = requests.request

    def send(self, method, url, kwargs):
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
        # final_kwargs = self.__login_auth(be, kwargs)

        #解包final_kwargs传入request方法
        r = self.request(method, url, **kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r
