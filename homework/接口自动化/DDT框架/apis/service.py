import json
import requests

from until.log import logger


class Service():

    def __init__(self):
        self.request = requests.request

    def run_step(self, step: dict):
        """
        解析字典解析发送方式，url,和参数。
        并检查是否有final_token需要进行拼装到参数中。
        调用send方法发出
        """
        pass

    def login_auth(self, step: dict):
        """
        获取登录鉴权，并赋予赋值给final_token
        """
        pass

    def send(self, method, url, kwargs: dict) -> object:
        """
        """
        # 解包kwargs传入request方法发送请求
        r = self.request(method, url, **kwargs)
        logger.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r
