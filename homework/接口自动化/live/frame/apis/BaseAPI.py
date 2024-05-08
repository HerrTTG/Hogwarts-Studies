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

    def send(self, method, url, kwargs: dict) -> object:
        """
        接口发送请求


        注意点：
        接口在调用send方法时，实际会被loginAuth的send方法先拦截。
        loginAuth在做完登录鉴权动作后，拼装鉴权信息，返回最终的final_kwargs。
        在调用此send方法，final_kwargs->kwargs
        所以kwargs为拼装鉴权信息后的字典,解包传入request请求中。

        包括login接口请求的send会直接拼装kwarge为字典，调用此send方法发送。
        """
        # 解包kwargs传入request方法发送请求
        r = self.request(method, url, **kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r
