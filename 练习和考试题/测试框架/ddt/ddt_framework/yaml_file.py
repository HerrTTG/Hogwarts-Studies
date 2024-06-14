import pytest as pytest

from ddt_framework.yaml_item import YamlItem


class YamlFile(pytest.File):
    def collect(self):
        # pytest会调用collect，获得每个文件的测试用例
        # YamlFile通过继承pytest.File 并复写collect来改写pytest收集测试用例的过程。
        # 返回是一个对象，则pytest会认为是一个可执行测试集
        import yaml

        # 先读取文件的结构 生成为dict
        raw = yaml.safe_load(self.path.open())
        if raw:
            for name, spec in sorted(raw.items()):
                # 对每个kv结构生成Item对象
                """
                如：
                ok:
                    sub1: sub2
                ok这个顶层的key被当做name作为测试用例名，
                后续的sub1 :sub2 座位测试步骤
                """
                yield YamlItem.from_parent(self, name=name, spec=spec)
