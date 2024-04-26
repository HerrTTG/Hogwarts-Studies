import allure
import jsonpath
import logging
import pytest
import requests


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

    def test_query_sub_department(self, precondition):

        self.params, self.deparment_info = precondition
        self.params["id"] = self.deparment_info["id"]
        r2 = requests.request('GET', 'https://qyapi.weixin.qq.com/cgi-bin/department/simplelist',
                              params=self.params, verify=False)

        print(r2.text)
