import allure
import jsonpath
import logging
import pytest
import sys
import yaml

sys.path.append('..\\..\\..\\live')

from frame.apis.Address_book.department import Department
from frame.untils.JsonShema import My_jsonschema
from frame.untils.Dbquery import Dblink
from frame.untils.until import Untils


@pytest.fixture(scope='class')
def operator(request):
    """
    测试装置，完成测试前环境信息的获取。对象的创建。
    完成测试后数据的清理
    """
    # 根据命令行获取，从不同的配置文件中获取环境信息
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print('获取并返回环境信息，此条为测试环境')
        with open(f'{Untils.get_path()}\\frame\\config\\envtest.yaml', 'r') as file:
            envinfo = yaml.safe_load(file)
    elif myenv == 'dev':
        print('获取并返回环境信息，此条为开发环境')
        with open(f'{Untils.get_path()}\\frame\\config\\devtest.yaml', 'r') as file:
            envinfo = yaml.safe_load(file)
    logging.debug(f'用例执行环境信息为:{envinfo}')

    # 测试准备
    # 实例化接口对象
    tester = Department(envinfo)
    # 实例化数据库对象
    dblink = Dblink(envinfo)

    # 测试数据准备
    departdata = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 2}

    logging.debug(f'用例测试数据:{departdata}')

    yield tester, dblink, departdata

    """
    数据清理
    """
    logging.info(f'测试数据清理')

    # 发送删除接口请求
    r3 = tester.delete({'id': departdata['id']})

    # 生成jsonschmea
    My_jsonschema().generate_jsonschema_file(r3.json(),
                                             filepath=f'{Untils.get_path()}\\frame\\config\\delete.json')

    # 断言
    try:
        result = My_jsonschema().jsonschema_valida_file(r3.json(),
                                                        filepath=f'{Untils.get_path()}\\frame\\config\\delete.json')
        assert result is True
        if jsonpath.jsonpath(r3.json(), '$..errcode')[0] == 60123:
            logging.warning(f'清理数据失败,被删除部门不存在.响应信息{r3.json()}')
            pass
        else:
            assert jsonpath.jsonpath(r3.json(), '$..errcode')[0] == 0
            assert jsonpath.jsonpath(r3.json(), '$..errmsg')[0] == 'deleted'
    except AssertionError:
        logging.error(f'清理数据失败,响应信息{r3.json()}')
        raise AssertionError


class Testcase():
    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('通讯录部门管理')
    @allure.title('企业微信添加部门接口测试')
    def test_deparment(self, operator):
        """
        1. 测试用例根据功能进行分层设计。(框架化)
        2. 通过企业微信接口文档获取登录权限 access_token，并进行响应断言。
        3. 创建部门，传入上一个接口的结果数据access_token，并使用jsonpath表达式获取响应结果的errmsg进行断言。
        4. 获取子部门ID列表，响应结果使用jsonschame进行断言验证。
        5. 生成对应的allure报告，显示log日志打印输出获取的access_token值。
        """

        logging.info(f'测试用例:企业微信添加部门接口测试')
        self.tester, self.dblink, self.departdata = operator

        with allure.step('测试步骤一:增加子部门'):
            # 发送请求
            r1 = self.tester.create(self.departdata)
            # 生成jsonchema
            My_jsonschema().generate_jsonschema_file(r1.json(),
                                                     filepath=f'{Untils.get_path()}\\frame\\config\\create.json')

            # 开始断言
            try:
                result = My_jsonschema().jsonschema_valida_file(r1.json(),
                                                                filepath=f'{Untils.get_path()}\\frame\\config\\create.json')
                assert result is True
                assert jsonpath.jsonpath(r1.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r1.json(), '$..errmsg')[0] == 'created'
                assert jsonpath.jsonpath(r1.json(), '$..id')[0] == self.departdata['id']
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败，jsonschema结果为{result}")
                logging.error(f"errcode:{jsonpath.jsonpath(r1.json(), '$..errcode')}")
                logging.error(f"errmsg:{jsonpath.jsonpath(r1.json(), '$..errmsg')}")
                logging.error(f"id:{jsonpath.jsonpath(r1.json(), '$..id')}")
                raise AssertionError

        with allure.step('测试步骤二:查询子部门'):
            # 发送请求
            r2 = self.tester.simplelist({'id': self.departdata['id']})
            # 生成jsonchema
            My_jsonschema().generate_jsonschema_file(r2.json(),
                                                     filepath=f'{Untils.get_path()}\\frame\\config\\simplelist.json')

            # 开始断言
            try:
                result = My_jsonschema().jsonschema_valida_file(r2.json(),
                                                                filepath=f'{Untils.get_path()}\\frame\\config\\simplelist.json')
                assert result is True
                assert jsonpath.jsonpath(r2.json(), '$..id')[0] == self.departdata['id']
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败,jsonschema结果为{result}")
                logging.error(f"id:{jsonpath.jsonpath(r2.json(), '$..id')}")
                raise AssertionError

        with allure.step('测试步骤三:测试数据库'):
            # 执行sql
            res = self.dblink.execute_sql("select * from students;")

            # 检查结果
            print(res.fetchall())
