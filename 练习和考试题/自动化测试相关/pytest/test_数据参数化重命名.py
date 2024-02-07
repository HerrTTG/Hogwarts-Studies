import pytest
import yaml

# 读取yaml文件的数据参数
with open("data.yaml", "r") as file:
    data = yaml.safe_load(file)


# 被测函数
def add(a, b):
    return a + b


# 测试用例，利用数据驱动方法DDT的测试方式。从data列表中传入参数给用例。用例调用方法。
# ids 参数为用例重命名。ids列表参数的个数要与数据参数的个数一致。
# 必须一一对应。比如有5组数据就要有5个重命名
# 中文重命名需要conftest文件
@pytest.mark.parametrize("a, b, expect", data, ids=['1+2=3', '4+5=9', '7+8=15', '中文测试'])
def test_add(a, b, expect):
    assert add(a, b) == expect, '与预期结果不符'
