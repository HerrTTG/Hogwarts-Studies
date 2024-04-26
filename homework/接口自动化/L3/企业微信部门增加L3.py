import allure
import json
import jsonpath
import logging
import pytest
import requests
from genson import SchemaBuilder
from jsonschema.validators import validate


class My_jsonschema():
    @classmethod
    def generate_jsonschema(cls, obj):
        # 实例化SchemaBuilder类
        builder = SchemaBuilder()
        # 调用add_object方法将json数据传入
        builder.add_object(obj)

        return builder.to_schema()

    @classmethod
    def generate_jsonschema_file(cls, obj, filepath='./jsonchema.json'):
        # 实例化SchemaBuilder类
        builder = SchemaBuilder()
        # 调用add_object方法将json数据传入
        builder.add_object(obj)
        # 返回为schema格式的json文件
        with open(filepath, 'w') as f:
            json.dump(builder.to_schema(), f)

    @classmethod
    def jsonschema_valida(cls, instobj, schema):
        try:
            validate(instance=instobj, schema=schema)
            return True
        except:
            return False

    @classmethod
    def jsonschema_valida_file(cls, instobj, filepath='./jsonchema.json'):
        with open(filepath, "r") as f:
            schema = json.load(f)
        try:
            validate(instance=instobj, schema=schema)
            return True
        except Exception as e:
            return False


class Test_wexin_department:

    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('通讯录部门管理')
    @allure.title('企业微信添加部门接口测试')
    def test_add_department(self, precondition):
        """
        冒烟测试，基础功能，从fixture获取添加部门信息和token.
        注意gettoken请求的参数中corpsecret要为通讯录模块的，并且提前将本机ip加入可信列表中。否则会获取token失败。
        """
        self.params, self.deparment_info = precondition

        logging.info(f'测试开始:企业微信添加部门接口测试')
        with allure.step('测试步骤一:发送增加部门请求'):
            logging.info(f'测试步骤一:发送增加部门请求')
            r = requests.request('POST', 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
                                 params=self.params, json=self.deparment_info, verify=False)
            logging.info(f'增加部门请求响应结果：{r.text}')

        with allure.step('测试步骤二:断言测试结果'):
            logging.info(f'测试步骤二:断言测试结果')
            try:
                assert r.status_code == 200
            except AssertionError:
                logging.debug(f'测试步骤二:断言测试结果失败，响应码{r.status_code}')
                raise '测试步骤二:断言测试结果失败'
            else:
                try:
                    assert jsonpath.jsonpath(r.json(), "$..errcode")[0] == 0
                    assert jsonpath.jsonpath(r.json(), "$..errmsg")[0] == 'created'
                except AssertionError:
                    logging.debug(
                        f'测试步骤二:断言测试结果失败，expect errcode ：0 实际结果 {jsonpath.jsonpath(r.json(), "$..errcode")} expect errmsg：created 实际结果{jsonpath.jsonpath(r.json(), "$..errmsg")[0]}')
                    raise AssertionError
                else:
                    try:
                        assert jsonpath.jsonpath(r.json(), "$..id")[0] == self.deparment_info["id"]
                    except AssertionError:
                        logging.debug(
                            f'expect id ：{self.deparment_info["id"]} 实际结果{jsonpath.jsonpath(r.json(), "$..id")[0]}')
                        raise AssertionError

        with allure.step('测试步骤三:断言整体结构'):
            logging.info(f'测试步骤三:断言整体结构')
            res_simple = {"errcode": 0, "errmsg": "created", "id": 2}
            vs_inst = My_jsonschema.generate_jsonschema(res_simple)
            logging.info(f'JSONschema:{vs_inst}')
            try:
                assert My_jsonschema.jsonschema_valida(r.json(), vs_inst) == True
            except AssertionError:
                logging.debug(f'测试步骤三:整体结构断言失败，结果{My_jsonschema.jsonschema_valida(r.json(), vs_inst)}')

    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('通讯录部门管理')
    @allure.title('企业微信查询子部门接口测试')
    def test_query_sub_department(self, precondition):
        """
        冒烟测试，基础功能，从fixture获取部门信息和token.
        注意gettoken请求的参数中corpsecret要为通讯录模块的，并且提前将本机ip加入可信列表中。否则会获取token失败。
        """

        self.params, self.deparment_info = precondition
        self.params["id"] = self.deparment_info["id"]
        logging.info(f'测试开始:企业微信查询子部门接口测试')

        with allure.step('测试步骤一:发送查询部门请求'):
            logging.info(f'测试步骤一:发送查询部门请求')
            r2 = requests.request('GET', 'https://qyapi.weixin.qq.com/cgi-bin/department/simplelist',
                                  params=self.params, verify=False)
            logging.info(f'增加部门请求响应结果：{r2.text}')

        with allure.step('测试步骤二:断言测试结果'):
            logging.info(f'测试步骤二:断言测试结果')
            try:
                assert r2.status_code == 200
            except AssertionError:
                logging.debug(f'测试步骤二:断言测试结果失败，响应码{r2.status_code}')
                raise '测试步骤二:断言测试结果失败'

            else:
                try:
                    assert self.deparment_info["id"] in jsonpath.jsonpath(r2.json(), "$..id")
                except AssertionError:
                    logging.debug(
                        f'expect id ：{self.deparment_info["id"]} 实际结果{jsonpath.jsonpath(r2.json(), "$..id")[0]}')
                    raise AssertionError

        with allure.step('测试步骤三:断言整体结构'):
            logging.info(f'测试步骤三:断言整体结构')
            res_simple = {"errcode": 0, "errmsg": "ok", "department_id": [{"id": 2, "parentid": 1, "order": 1}]}
            vs_inst = My_jsonschema.generate_jsonschema(res_simple)
            logging.info(f'JSONschema:{vs_inst}')
            try:
                assert My_jsonschema.jsonschema_valida(r2.json(), vs_inst) == True
            except AssertionError:
                logging.debug(f'测试步骤三:整体结构断言失败，结果{My_jsonschema.jsonschema_valida(r2.json(), vs_inst)}')
