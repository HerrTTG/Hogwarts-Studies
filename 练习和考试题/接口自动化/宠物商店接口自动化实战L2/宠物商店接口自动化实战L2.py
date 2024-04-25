import allure
import jsonpath
import logging
import requests


class Test_case:

    @allure.feature('宠物商店')
    @allure.story('宠物管理系统')
    @allure.title('宠物管理系统增删改查')
    def test_pet_interface(self, envget, dataload):
        logging.info("参数初始化开始")
        baseurl = envget + '/pet'
        pet_id, pet_status, add_pet_info, update_name, update_pet_info, search_param, proxy = dataload
        # print(pet_id, pet_status, add_pet_info, update_name, update_pet_info, search_param, proxy)
        logging.info({'baseurl': baseurl, 'pet_id': pet_id,
                      'pet_status': pet_status, 'add_pet_info': add_pet_info,
                      'update_name': update_name, 'update_pet_info': update_pet_info,
                      'search_param': search_param, 'proxy': proxy})
        with allure.step("测试步骤一，新增宠物"):
            # 新增宠物
            logging.info('测试步骤一，新增宠物')
            add_request = requests.request("POST", baseurl, json=add_pet_info, proxies=proxy, verify=False)
            logging.info(f"新增宠物接口响应为：{add_request.text}")
            try:
                assert add_request.status_code == 200
            except AssertionError:
                logging.debug(f"新增宠物接口请求响应断言失败,响应码：{add_request.status_code}")
                raise '查询宠物接口请求响应状态断言失败'

        with allure.step("测试步骤二，查询宠物"):
            # 查询宠物
            logging.info('测试步骤二，查询宠物')
            search_request = requests.request("GET", baseurl + "/findByStatus", params=search_param, proxies=proxy,
                                              verify=False)
            logging.info(f"查询宠物接口响应为：{search_request.text}")

            try:
                assert search_request.status_code == 200
            except AssertionError:
                logging.debug(f"查询宠物接口请求响应断言失败,响应码：{search_request.status_code}")
                raise '查询宠物接口请求响应状态断言失败'
            else:
                try:
                    assert pet_id in jsonpath.jsonpath(search_request.json(), "$..id")
                except AssertionError:
                    logging.debug(
                        f"查询宠物接口请求响应内容断言失败,expect pet id ：{pet_id},实际结果：{jsonpath.jsonpath(search_request.json(), '$..id')}")
                    raise '查询宠物接口请求响应内容断言失败,期望值与结果不符。'

        with allure.step("测试步骤三，修改宠物"):
            logging.info('测试步骤三，修改宠物')
            update_request = requests.request("PUT", baseurl, json=update_pet_info, proxies=proxy, verify=False)
            logging.info(f"修改宠物接口响应为：{update_request.text}")

            try:
                assert update_request.status_code == 200
            except AssertionError:
                logging.debug(f"更新宠物接口请求响应断言失败,响应码：{update_request.status_code}")
                raise '更新宠物接口请求响应状态断言失败'
            else:
                search_request = requests.request("GET", baseurl + "/findByStatus", params=search_param, proxies=proxy,
                                                  verify=False)
                logging.info(f"修改后的查询宠物接口响应为：{search_request.text}")

                try:
                    assert search_request.status_code == 200
                except AssertionError:
                    logging.debug(f"修改后查询宠物接口请求响应断言失败,响应码：{search_request.status_code}")
                    raise '修改后查询宠物接口请求响应状态断言失败'
                else:
                    try:
                        assert update_name in jsonpath.jsonpath(search_request.json(), '$.*.name')
                    except AssertionError:
                        logging.debug(
                            f"修改后查询宠物接口请求响应内容断言失败,expect update_name ：{update_name},实际结果：{jsonpath.jsonpath(search_request.json(), '$.*.name')}")
                        raise '修改后查询宠物接口请求响应内容断言失败,期望值与结果不符。'

        with allure.step("测试步骤四，删除宠物"):
            logging.info('测试步骤四，删除宠物')
            delete_request = requests.request("DELETE", baseurl + f"/{pet_id}", proxies=proxy, verify=False)
            logging.info(f"修改宠物接口响应为：{delete_request.text}")

            try:
                assert delete_request.status_code == 200
            except AssertionError:
                logging.debug(f"删除宠物接口请求响应断言失败,响应码：{delete_request.status_code}")
                raise '删除宠物接口请求响应状态断言失败'
            else:
                search_request = requests.request("GET", baseurl + "/findByStatus", params=search_param, proxies=proxy,
                                                  verify=False)
                logging.info(f"删除后的查询宠物接口响应为：{search_request.text}")

                try:
                    assert search_request.status_code == 200
                except AssertionError:
                    logging.debug(f"删除后查询宠物接口请求响应断言失败,响应码：{search_request.status_code}")
                    raise '删除后查询宠物接口请求响应状态断言失败'
                else:
                    try:
                        assert pet_id not in jsonpath.jsonpath(search_request.json(), '$..id')
                    except AssertionError:
                        logging.debug(
                            f"删除后查询宠物接口请求响应内容断言失败,expect pei id ：{pet_id} 不存在,实际结果：{jsonpath.jsonpath(search_request.json(), '$..id')}")
                        raise '删除后查询宠物接口请求响应内容断言失败,期望值与结果不符。'
