import allure
from pydantic import BaseModel
from typing import Any

from apis.service import Service
from collecter.yaml_exception import AssertException
from until.log import logger


class TestCase(BaseModel):
    # 利用模型的概念，定义一个testcase模型。

    # 声明一个testcase需要什么东西
    name: str = None
    # setup
    given: list[dict] = []
    # 测试步骤
    when: list[dict] = []
    # 断言
    then: list[dict] = []
    # 后置处理
    teardown: list[dict] = []

    def __init__(self, **spec: Any) -> None:
        ## 利用pydantic来做数据类型校验
        # 将传入data解包后，生成data对应selfname的对象变量
        # 定义接口对象为全局变量，并增加一个结果变量为空列表
        global service, result
        service = None
        result = []
        super().__init__(**spec)

    def run(self, name):
        """
        testcase的执行，对given when then teardown进行分化。调用__run_step单步执行。
        """
        allure.dynamic.title(f'run testcase {name}')
        logger.info(f'run testcase {name}')
        logger.info(f"run object {self}")

        # 按照given when then teardown的先后顺序执行
        ls = [self.given, self.when, self.then, self.teardown]
        for i in ls:
            for step in i:
                with allure.step(f"run step{step.keys()}"):
                    try:
                        assert self.__run_step(step)
                    except AssertionError:
                        raise AssertException(name, step)

    def __run_step(self, step: dict):
        """
        单步执行
        """
        logger.info(f"run step{step.keys()}")
        logger.info(f"run step object {step}")

        global service
        if service is None:
            service = Service()
            print(service)

        """
        {'auth': {'params': {'SECRET': 'A4I9cDIUfaIpJZZIDUdI88vMrC-NkhyFVbIEOnfS5VI', 'corpid': 'ww7f1ecbb8e23f2091'}, 'token': True, 'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'}}
        {'get': {'params': {}, 'url': 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners?lastName=black'}}
        {'assert': " 'Jeff' in self.result"}
        """

        if 'auth' in step and step['auth']['token'] == True:
            return service.login_auth(step)
        elif 'assert' in step and step['assert']:
            return eval(step['assert'])
        else:
            for mothod, request_kwargs in sorted(step.items()):
                result.append(service.request_analysis(mothod, request_kwargs))
            return result
