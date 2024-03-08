##https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
import allure
import logging
import requests


class Test_gettoken:

    @allure.feature('企业微信')
    @allure.story('授权')
    @allure.title('获取token用例')
    def test_get_weixin_token(self, logininfor):
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
