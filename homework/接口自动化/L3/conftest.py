'''
pytest的公共数据和方法模块。
将此文件和测试用例py文件放入一个文件夹内即可。
'''
import logging
import pytest
import requests


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


# 获取token权限
@pytest.fixture(scope='class')
def precondition():
    params = {'corpid': 'ww7f1ecbb8e23f2091', 'corpsecret': 'A4I9cDIUfaIpJZZIDUdI88vMrC-NkhyFVbIEOnfS5VI'}
    logging.info('测试前准备，获取token')
    r = requests.request("GET", 'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params, verify=False)
    logging.info(f'测试前准备，获取token接口的返回结果{r.text}')

    try:
        assert r.status_code == 200
    except AssertionError:
        logging.debug(f'获取token请求响应码断言失败,结果为{r.status_code == 200}')
        raise '获取token请求响应码断言失败'
    else:
        try:
            assert r.json()['access_token'] is not None
        except AssertionError:
            logging.debug(f'获取token请求响应体中未包含token信息,结果为{r.json()["access_token"]}')
            raise '获取token请求响应体中未包含token信息'
        else:
            logging.info('测试数据准备')
            deparment_info = {
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
                "id": 2
            }
            token = {'access_token': r.json()["access_token"]}
            logging.info(f'测试前准备结束，获取token:{token},部门信息{deparment_info}')

            yield token, deparment_info
            # 清理生成的数据
            logging.info(f'test DELETE')
