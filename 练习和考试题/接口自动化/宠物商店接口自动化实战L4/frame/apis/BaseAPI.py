"""
BaseAPI主要是定义接口的各种方法，后续API可以直接继承BaseAPI 类来实现方法的复用
"""
import json
import logging
import requests
from frame.untils.login import Loginrequest


class BaseAPI():
    """
    所有API的父类
    主要功能：
    构造函数生成各个属性以及实例化鉴权操作的对象
    获取token

    父类解决以下问题：
    # 问题1： 接口里面直接使用了requests
    # 解决方案： 在base_api中添加公共的send方法
    # 问题2：大量重复的host地址
    # 解决方案，在构造函数，实例化环境信息提供的host地址的url，并且在子类api调用send方法时，直接利用self.url拼装接口地址传入参数。
    # 优化3： token 的获取
    # 解决方案：父类中定义一个获取token方法，根据实例化时传入的role进行区分不同的登录鉴权操作。
              传入子类带入的参数，最后和包含token的header。返回给send的打包参数**kwargs 包含所需的所有参数。

    """

    def __init__(self, role, envinfo):
        """
        实例化信息
        创建登录对象
        """
        self.role = role
        self.url = envinfo['url']
        self.envinfo = envinfo
        self.auth = Loginrequest()

    def send(self, method, url, **kwargs):
        """
        API的发送请求方法
        kwargs为子类调用send方法时传入的所有所需参数，带入获取token方法中，最后一起封装为**kwargs传入request请求。
        """
        final_kwargs = self._get_token(kwargs)
        r = requests.request(method, url, **final_kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def _get_token(self, request_params):
        """
        根据不同的role 调用role_login方法进行登录操作。
        将返回的token封装进header中
        """
        if self.role == 'admin' and hasattr(self, 'final_token') is False:
            self.token = self.auth.role_login(self.url + "/admin/auth/login", 'admin', self.envinfo)
            self.final_token = {"X-Litemall-Admin-Token": self.token}
        elif self.role == 'wx' and hasattr(self, 'final_token') is False:
            self.token = self.auth.role_login(self.url + "/wx/auth/login", 'wx', self.envinfo)
            self.final_token = {"X-Litemall-Token": self.token}
        elif self.role == 'admin' and hasattr(self, 'final_token') is True:
            self.final_token = {"X-Litemall-Admin-Token": self.token}
        elif self.role == 'wx' and hasattr(self, 'final_token') is True:
            self.final_token = {"X-Litemall-Token": self.token}

        # 判断是否有headers信息，如果有，将token更新进去。如果没有，则赋值headers为token信息
        if request_params.get("headers"):
            request_params["headers"].update(self.final_token)
        else:
            request_params["headers"] = self.final_token
        return request_params
