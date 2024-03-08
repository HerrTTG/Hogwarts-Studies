'''
pytest的公共数据和方法模块。
将此文件和测试用例py文件放入一个文件夹内即可。
'''
import pytest


# hook函数
# 收集测试用例，收集之后（改编码，改执行顺序）
def pytest_collection_modifyitems(items: list):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    # item中是一个方法对象，此方法对象就是对应的测试用例了
    # name就是测试用例的名字
    # _nodeid测试用例的路径
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='class')
def logininfor():
    corpid = 'ww7f1ecbb8e23f2091'
    corpsecret = 'aDSsHNlF2CEN47rXIhVuW424FHGZ_t_OrRuPNXBQzoo'
    return corpid, corpsecret
