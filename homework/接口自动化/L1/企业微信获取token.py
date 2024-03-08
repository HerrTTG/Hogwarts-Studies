##https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
import allure
import logging
import pytest
import requests


class Test_gettoken:

    @pytest.mark.冒烟测试
    @allure.feature('企业微信')
    @allure.story('授权')
    @allure.title('冒烟测试获取token用例')
    def test_get_weixin_token(self, logininfor):
        """
        冒烟测试，基础功能，从fixture获取登录信息
        """
        baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        ID, SECRET = logininfor
        params = {
            "corpid": ID,
            "corpsecret": SECRET
        }

        with allure.step("测试步骤一:发送请求"):
            logging.info(f"开始测试步骤一，发送请求.url:{baseurl},params:{params}")
            r = requests.request('GET', baseurl, params=params)

        with allure.step("测试步骤二:断言结果"):
            logging.info(f"开始测试步骤二，断言结果。")
            try:
                assert r.status_code == 200
                assert r.json()['access_token'] is not None
            except:
                logging.error(f"测试失败")
                raise
            else:
                # print(r.json()['access_token'])
                logging.info('token:' + r.json()['access_token'])

    @pytest.mark.错误推测
    @allure.feature('企业微信')
    @allure.story('授权')
    @allure.title('获取token用例，输入不正确')
    @pytest.mark.parametrize('ID', ['', '1', '!%^#![]'])
    @pytest.mark.parametrize('SECRET', ['2', '', '!%^#![]'])
    def test_get_weixin_token_2(self, ID, SECRET):
        """
        异常用例，输出缺少，或者输入错误的内容，包含特殊字符。
        使用笛卡尔积参数化数据驱动作为输入。
        """
        baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            "corpid": ID,
            "corpsecret": SECRET
        }

        with allure.step("测试步骤一:发送请求"):
            logging.info(f"开始测试步骤一，发送请求.url:{baseurl},params:{params}")
            r = requests.request('GET', baseurl, params=params)

        with allure.step("测试步骤二:断言结果"):
            logging.info(f"开始测试步骤二，断言结果。")
            try:
                assert r.status_code == 200
                assert r.json()["errcode"] in [40013, 41002, 41004]
            except:
                logging.error(f"测试失败")
                logging.info(r.text)
                raise
            else:
                jsondata = r.json()
                logging.info(f'{jsondata["errcode"]},{jsondata["errmsg"]}')
