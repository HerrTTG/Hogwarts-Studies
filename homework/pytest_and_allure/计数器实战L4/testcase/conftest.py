import logging
import pytest


# hook函数
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


# 给pytest添加自定义命令行参数
def pytest_addoption(parser):
    # parser
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量，为属性命令，可以使用Option对象访问到这个值，暂用不到
                      help='set your run env'  # 帮助提示 参数的描述信息
                      )


@pytest.fixture(scope='session', autouse=True)
def envget(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        logging.info('获取并返回环境信息，此条为测试环境')
    elif myenv == 'dev':
        logging.info('获取并返回环境信息，此条为开发环境')
