'''
将此文件和测试用例py文件放入一个文件夹内即可。
'''
import pytest

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


# 定义在conftest中的方法是公共的 并且不需要引用。
@pytest.fixture(scope="module")
def loing():
    print("登录完成")
    token = '12341231'
    userid = 'kuoka'
    # yield 相当于return 可以同时带数据返回
    yield token, userid
    print('登录结束')
