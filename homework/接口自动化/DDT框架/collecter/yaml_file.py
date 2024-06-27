import pytest as pytest

from collecter.yaml_item import YamlItem


class YamlFile(pytest.File):
    def collect(self):
        # pytest会调用collect，获得每个文件的测试用例
        # YamlFile通过继承pytest.File 并复写collect来改写pytest收集测试用例的过程。
        # 返回是一个对象，则pytest会认为是一个可执行测试集
        import yaml

        # 先读取文件的结构 生成为dict
        raw = yaml.safe_load(self.path.open('r', encoding='utf-8'))
        if raw:
            for name, spec in sorted(raw.items()):
                # 对每个kv结构生成Item对象
                """
                取出
                case1(name):...(spec)
                """
                yield YamlItem.from_parent(self, name=name, spec=spec)
