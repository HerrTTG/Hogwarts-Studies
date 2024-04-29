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
    # 解决方案： 在base_api中添加公共的send方法。子类api直接使用send方法发送请求。
    # 问题2：大量重复的host地址
    # 解决方案，在构造函数，实例化环境信息提供的host地址的url，并且在子类api调用send方法时，直接利用self.url拼装接口地址传入参数。
    # 优化3： token 的获取
    # 解决方案：父类中定义一个获取token方法，根据实例化时传入的role进行区分不同的登录鉴权操作。
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
        final_kwargs = self.__get_token(kwargs)
        r = requests.request(method, url, **final_kwargs)
        logging.debug(f"{url}接口的响应为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def __get_token(self, request_params):
        """
        # 问题1： 除登录接口之外，基本每一个接口，都需要另外去设置token
        # 解决方案：
        1. 在发起接口请求之前，就获取token信息
        2. 获取token信息之后，塞入到请求信息之中
        3. 除了method 和url 之外，所有的其他信息，包括header params 等等的其他参数，都会塞入至kwargs 不定长参数中
                cart_api -> send-> 获取kwargs -> 在kwargs 中 塞入header（鉴权）信息
        # 问题2: 如果有两个token存在怎么办？
        # 解决方案：
        # 1. 不同的角色有不同的token信息
        # 2. 根据不同的角色封装不同的token到header中

        # 问题3:每次请求接口都需要重复获取token
        # 解决方案：
        # 1.同样角色的token只在第一次尚未获取到token值时发送登录请求获取token
        # 2.后续同角色的接口都直接使用同样的token，不发送登录请求。
        """
        # 创建API接口的调用对象时，会传入role角色。并且生成不同的对象self
        # goods和cart的对象是不同的，所拥有的属性final_token亦是不同的
        # 判断self.final_token是否已经在，如果存在就不发送登录请求。直接根据角色的不同拼装不同的token
        # 如果不存在就先发送登录请求.
        # 这样admin 和wx只在他们各自首次调用api时，会去做登录操作获取token。后续同role的接口直接使用前面获取的token
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
