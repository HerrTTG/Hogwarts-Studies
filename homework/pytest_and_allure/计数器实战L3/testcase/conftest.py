import datetime
import pytest


@pytest.fixture(scope='session', autouse=True)
def sayhell0():
    print('测试开始~')
    starttime = datetime.datetime.now()
    yield
    print('测试结束~')
    endtime = datetime.datetime.now()
    print(f"耗时：{endtime - starttime}")
