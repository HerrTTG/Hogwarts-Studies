import pytest

from collecter.testcase import TestCase
from collecter.yaml_exception import YamlException
from until.log import logger


class YamlItem(pytest.Item):
    ## 测试用例的定义
    ## YamlItem 继承pytest.Item 并复写runtest 和repr_failure以及reportinfo 来实现定制化pytest用例的执行过程
    ## 首先定制化runtest。使yaml文件的数据变成真正的测试步骤
    def __init__(self, *, spec, **kwargs):
        """
        测试用例的定义，需要有测试用例的名字和内容
        spec：测试用例步骤
        name：测试名称
        """
        # 父类将name初始化给self.name
        super().__init__(**kwargs)
        # 用例步骤初始化
        self.spec = spec
        logger.debug(f"测试步骤{self.spec}")

        # 类型化测试用例
        self.testcase: TestCase = TestCase(**spec)
        logger.debug(f"测试用例实例{self.testcase}")

    def runtest(self):
        # 直接交给testcase自己去执行用例
        self.testcase.run()

    def repr_failure(self, excinfo):
        ##异常捕获。
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return "\n".join(
                [
                    "usecase execution failed",
                    "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                    "   no further details known at this point.",
                ]
            )
        else:
            logger.info(excinfo.value)
            raise excinfo.value

    def reportinfo(self):
        return self.path, 0, f"usecase: {self.name}"
