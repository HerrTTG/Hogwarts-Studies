import pytest

from ddt_framework.yaml_exception import YamlException


class YamlItem(pytest.Item):
    ## YamlItem 继承pytest.Item 并复写runtest 和repr_failure以及reportinfo 来实现定制化pytest用例的执行过程
    ## 首先定制化runtest。使yaml文件的数据变成真正的测试步骤
    def __init__(self, *, spec, **kwargs):
        """
        测试用例的定义，需要有测试用例的名字和内容
        """
        # 父类将name初始化给self.name
        super().__init__(**kwargs)
        # 用例步骤初始化
        self.spec = spec

    def runtest(self):
        # 简单的用例执行
        # 获取用例步骤中的kv。即key为期望值，value为实际值
        # 做的简单测试就是对比是否一致。
        for name, value in sorted(self.spec.items()):
            # Some custom test execution (dumb example follows).
            if name != value:
                raise YamlException(self, name, value)

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

    def reportinfo(self):
        return self.path, 0, f"usecase: {self.name}"
