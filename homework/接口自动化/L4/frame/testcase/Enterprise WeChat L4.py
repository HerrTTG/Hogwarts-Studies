import allure
import jsonpath
import logging
import pytest
import sys

sys.path.append('..\\..\\..\\L4')

from frame.apis.Address_book.department import Department
from frame.untils.JsonShema import My_jsonschema


class Testcase():
    def envmount(self, envinfo):
        """实例化接口对象，传入环境信息"""
        self.tester = Department(envinfo)

    def setup_class(self):
        """
        测试数据准备
        """
        self.departdata = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2}

        logging.debug(f'用例测试数据:{self.departdata}')

    def teardown(self):
        """
        数据清理
        """
        logging.info(f'测试数据清理')

        departid = {'id': self.departdata['id']}

        r3 = self.tester.delete(departid)
        # My_jsonschema().generate_jsonschema_file(r3.json(),filepath='../config/delete.json')
        try:
            assert My_jsonschema().jsonschema_valida_file(r3.json(), filepath='../config/delete.json') is True
            if jsonpath.jsonpath(r3.json(), '$..errcode')[0] == 60123:
                logging.warning(f'清理数据失败,被删除部门不存在.响应信息{r3.json()}')
                pass
            else:
                assert jsonpath.jsonpath(r3.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r3.json(), '$..errmsg')[0] == 'deleted'
        except AssertionError:
            logging.error(f'清理数据失败,响应信息{r3.json()}')
            raise AssertionError

    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('通讯录部门管理')
    @allure.title('企业微信添加部门接口测试')
    def test_deparment(self, envget):
        """
        1. 测试用例根据功能进行分层设计。(框架化)
        2. 通过企业微信接口文档获取登录权限 access_token，并进行响应断言。
        3. 创建部门，传入上一个接口的结果数据access_token，并使用jsonpath表达式获取响应结果的errmsg进行断言。
        4. 获取子部门ID列表，响应结果使用jsonschame进行断言验证。
        5. 生成对应的allure报告，显示log日志打印输出获取的access_token值。
        """
        logging.info(f'测试用例:企业微信添加部门接口测试')

        # 根据命令行获取，从不同的配置文件中获取环境信息
        self.envmount(envget)
        logging.debug(f'用例执行环境信息为:{envget}')

        with allure.step('测试步骤一:增加子部门'):
            r1 = self.tester.create(self.departdata)
            # My_jsonschema().generate_jsonschema_file(r1.json(),filepath='../config/create.json')
            try:
                assert My_jsonschema().jsonschema_valida_file(r1.json(), filepath='../config/create.json') is True
                assert jsonpath.jsonpath(r1.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r1.json(), '$..errmsg')[0] == 'created'
                assert jsonpath.jsonpath(r1.json(), '$..id')[0] == self.departdata['id']
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败，jsonschema结果为{My_jsonschema().jsonschema_valida_file(r1.json(), filepath='../config/create.json')}")
                logging.error(f"errcode:{jsonpath.jsonpath(r1.json(), '$..errcode')}")
                logging.error(f"errmsg:{jsonpath.jsonpath(r1.json(), '$..errmsg')}")
                logging.error(f"id:{jsonpath.jsonpath(r1.json(), '$..id')}")
                raise AssertionError

        with allure.step('测试步骤二:查询子部门'):
            r2 = self.tester.simplelist({'id': self.departdata['id']})
            # My_jsonschema().generate_jsonschema_file(r2.json(),filepath='../config/simplelist.json')
            try:
                assert My_jsonschema().jsonschema_valida_file(r2.json(), filepath='../config/simplelist.json') is True
                assert jsonpath.jsonpath(r2.json(), '$..id')[0] == self.departdata['id']
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败,jsonschema结果为{My_jsonschema().jsonschema_valida_file(r2.json(), filepath='../config/simplelist.json')}")
                logging.error(f"id:{jsonpath.jsonpath(r2.json(), '$..id')}")
                raise AssertionError
