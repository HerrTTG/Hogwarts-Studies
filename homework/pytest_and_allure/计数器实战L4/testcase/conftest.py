import logging
import pytest


# hook函数
# encode中文
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


@pytest.fixture(scope='session', autouse=True)
def envget(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        logging.info('获取并返回环境信息，此条为测试环境')
    elif myenv == 'dev':
        logging.info('获取并返回环境信息，此条为开发环境')
