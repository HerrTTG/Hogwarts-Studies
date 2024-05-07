import allure
import jsonpath
import logging
import pytest
import sys

sys.path.append('..\\..\\..\\live')

from frame.apis.Address_book.department import Department
from frame.apis.Address_book.member import Memebr
from frame.untils.JsonShema import My_jsonschema
from frame.untils.Dbquery import Dblink
from frame.untils.until import Untils


class Testcase():

    @pytest.fixture(scope='class')
    def operator(self, request):
        """
        测试装置，完成测试前环境信息的获取。对象的创建。
        完成测试后数据的清理
        """

        ## setup

        # 环境获取
        envinfo = Untils.get_env(request=request)
        logging.debug(f'用例执行环境信息为:{envinfo}')

        # 测试准备
        # 实例化对象
        self.department = Department(envinfo)
        self.member = Memebr(envinfo)
        self.dblink = Dblink(envinfo)

        # 测试数据准备
        self.departdata, self.memberdata = Untils.get_testdata()
        logging.debug(f'用例测试数据:{self.departdata},{self.memberdata}')

        # 返回对象
        yield self

        ## teardown

        logging.info(f'测试数据清理')

        # 发送删除接口请求
        r3 = self.department.delete({'id': self.departdata['id']})
        r6 = self.member.delete({'userid': self.memberdata['userid']})

        # 断言
        try:
            if jsonpath.jsonpath(r3.json(), '$..errcode')[0] == 60123:
                logging.warning(f'清理数据失败,被删除部门不存在.响应信息{r3.json()}')
                pass
            else:
                assert jsonpath.jsonpath(r3.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r3.json(), '$..errmsg')[0] == 'deleted'

            if jsonpath.jsonpath(r6.json(), '$..errcode')[0] == 60111:
                logging.warning(f'清理数据失败,被删除成员不存在.响应信息{r6.json()}')
                pass
            else:
                assert jsonpath.jsonpath(r6.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r6.json(), '$..errmsg')[0] == 'deleted'

        except AssertionError:
            logging.error(f'清理数据失败,响应信息{r3.json()}------{r6.json()}')
            raise AssertionError

    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('通讯录部门管理')
    @allure.title('企业微信添加部门接口测试')
    def test_deparment1(self, operator):
        """
        1. 测试用例根据功能进行分层设计。(框架化)
        2. 通过企业微信接口文档获取登录权限 access_token，并进行响应断言。
        3. 创建部门，传入上一个接口的结果数据access_token，并使用jsonpath表达式获取响应结果的errmsg进行断言。
        4. 获取子部门ID列表，响应结果使用jsonschame进行断言验证。
        5. 生成对应的allure报告，显示log日志打印输出获取的access_token值。
        """

        logging.info(f'测试用例:企业微信添加部门接口测试')

        with allure.step('测试步骤一:增加子部门'):
            # 发送请求
            r1 = operator.department.create(operator.departdata)
            # 生成jsonchema
            # My_jsonschema().generate_jsonschema_file(r1.json(),
            #                                          filepath=f'{Untils.get_path()}\\frame\\datas\\create.json')

            # 开始断言
            try:
                result = My_jsonschema().jsonschema_valida_file(r1.json(),
                                                                filepath=f'{Untils.get_path()}\\frame\\datas\\create.json')
                assert result is True
                assert jsonpath.jsonpath(r1.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r1.json(), '$..errmsg')[0] == 'created'
                assert jsonpath.jsonpath(r1.json(), '$..id')[0] == operator.departdata['id']
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败，jsonschema结果为{result}")
                logging.error(f"errcode:{jsonpath.jsonpath(r1.json(), '$..errcode')}")
                logging.error(f"errmsg:{jsonpath.jsonpath(r1.json(), '$..errmsg')}")
                logging.error(f"id:{jsonpath.jsonpath(r1.json(), '$..id')}")
                raise AssertionError

        with allure.step('测试步骤二:查询子部门'):
            # 发送请求
            r2 = operator.department.simplelist({'id': operator.departdata['id']})
            # 生成jsonchema
            # My_jsonschema().generate_jsonschema_file(r2.json(),
            #                                          filepath=f'{Untils.get_path()}\\frame\\datas\\simplelist.json')

            # 开始断言
            try:
                result = My_jsonschema().jsonschema_valida_file(r2.json(),
                                                                filepath=f'{Untils.get_path()}\\frame\\datas\\simplelist.json')
                assert result is True
                assert jsonpath.jsonpath(r2.json(), '$..id')[0] == operator.departdata['id']
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败,jsonschema结果为{result}")
                logging.error(f"id:{jsonpath.jsonpath(r2.json(), '$..id')}")
                raise AssertionError

        with allure.step('测试步骤三:测试数据库'):
            # 执行sql
            res = operator.dblink.execute_sql("select * from students;")

            # 检查结果
            print(res.fetchall())

    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('通讯录部门管理')
    @allure.title('企业微信部门成员查询')
    def test_deparment2(self, operator):
        """
        完成接口自动化测试框架搭建
        添加获取部门成员 ID 7的场景
        添加复杂断言
        使用 JSONPath 断言
        使用 JSONSchema 断言
        添加多环境配置
        添加数据清理步骤
        添加日志
        添加测试报告
        数据库断言
        """
        logging.info(f'测试用例:企业微信部门成员查询')

        with allure.step('测试步骤一:增加成员'):

            r4 = operator.member.create(operator.memberdata)
            # 开始断言
            try:
                assert jsonpath.jsonpath(r4.json(), '$..errcode')[0] == 0
                assert jsonpath.jsonpath(r4.json(), '$..errmsg')[0] == 'created'
            except AssertionError:
                logging.error(f"测试步骤一断言失败")
                logging.error(f"errcode:{jsonpath.jsonpath(r4.json(), '$..errcode')}")
                logging.error(f"errmsg:{jsonpath.jsonpath(r4.json(), '$..errmsg')}")
                raise AssertionError

        with allure.step('测试步骤二:查询成员'):
            r5 = operator.member.list({"limit": 10000})
            # 生成jsonchema
            # My_jsonschema().generate_jsonschema_file(r5.json(),
            #                                           filepath=f'{Untils.get_path()}\\frame\\datas\\memberlist.json')

            # 开始断言
            try:
                result = My_jsonschema().jsonschema_valida_file(r5.json(),
                                                                filepath=f'{Untils.get_path()}\\frame\\datas\\memberlist.json')
                assert result is True
                assert operator.memberdata['userid'] in jsonpath.jsonpath(r5.json(), '$..userid')
            except AssertionError:
                logging.error(
                    f"测试步骤一断言失败,jsonschema结果为{result}")
                logging.error(f"id:{jsonpath.jsonpath(r5.json(), '$..open_userid')}")
                raise AssertionError
