from pydantic import BaseModel
from typing import Any

from apis.service import Service
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

    def __init__(self, **data: Any) -> None:
        ## 利用pydantic来做数据类型校验
        # 将传入data解包后，生成data对应selfname的对象变量
        global service
        service = None
        super().__init__(**data)

    def run(self):
        """
        testcase的执行，对given when then teardown进行分化。调用__run_step单步执行。
        """
        logger.info('run testcase')
        logger.info(self)

        # 按照given when then的先后顺序执行
        logger.info('run testcase given')
        logger.info(self.given)
        # step 在这里就是given的value
        for step in self.given:
            self.__run_step(step)

        logger.info('run testcase when')
        logger.info(self.when)
        for step in self.when:
            self.__run_step(step)

        logger.info('run testcase then')
        logger.info(self.then)
        for step in self.then:
            self.__run_step(step)

        logger.info('run testcase teardown')
        logger.info(self.teardown)
        for step in self.teardown:
            self.__run_step(step)

    def __run_step(self, step: dict):
        """
        单步执行
        """
        logger.info('run step')
        logger.info(step)

        global service
        if service is None:
            service = Service()

        """
        {'auth': {'SECRET': 'A4I9cDIUfaIpJZZIDUdI88vMrC-NkhyFVbIEOnfS5VI', 'corpid': 'ww7f1ecbb8e23f2091', 'token': True}}
        {'get': {'params': {}, 'url': 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners?lastName=black'}}
        {'assert': " 'Jeff' in self.result"}
        """

        if 'auth' in step and step['auth']['token'] == True:
            service.login_auth(step)
        elif 'assert' in step and step['assert']:
            assert eval(step['assert'])
        else:
            service.run_step(step)
