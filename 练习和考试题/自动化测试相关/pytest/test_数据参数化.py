import pytest
import yaml

# 读取yaml文件的数据参数
with open("data.yaml", "r") as file:
    data = yaml.safe_load(file)


# 被测函数
def add(a, b):
    return a + b


# 测试用例，利用数据驱动方法DDT的测试方式。从data列表中传入参数给用例。用例调用方法。
@pytest.mark.parametrize("a, b, expect", data)
def test_add(a, b, expect):
    assert add(a, b) == expect, '与预期结果不符'
