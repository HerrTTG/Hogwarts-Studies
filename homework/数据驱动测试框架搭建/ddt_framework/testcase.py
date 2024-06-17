from pydantic import BaseModel
from typing import Any

from ddt_framework.service import Service
from ddt_framework.utils import log
from ddt_framework.web import Web


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
        super().__init__(**data)

    def run(self):
        """
        testcase的执行，对given when then进行分化。调用steprun单步执行。
        """
        log.info('run testcase')
        log.info(self)

        # 按照given when then的先后顺序执行
        log.info(self.given)
        # step 在这里就是given的value
        for step in self.given:
            self.__run_step(step)

        log.info('run testcase when')
        log.info(self.when)
        for step in self.when:
            self.__run_step(step)

        log.info(self.then)
        for step in self.then:
            self.__run_step(step)

        log.info(self.teardown)
        for step in self.teardown:
            self.__run_step(step)

    def __run_step(self, step: dict):
        """
        单步执行
        """
        global web, service
        log.info('run step')
        log.info(step)

        # 创建web和接口对象 当为空时
        if web is None:
            web = Web()

        if service is None:
            service = Service()

        # 调用web对象的用用的run_step
        if web.run_step(step):
            return

        if service.run_step(step):
            log.info(service.result)
            return
