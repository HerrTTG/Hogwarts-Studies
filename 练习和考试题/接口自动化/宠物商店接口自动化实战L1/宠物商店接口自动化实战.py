import allure
import logging
import pytest
import requests


class Test_serch:
    @pytest.mark.冒烟测试
    @allure.feature('宠物商店')
    @allure.story('查询接口')
    @allure.title('冒烟测试根据状态获取宠物信息')
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_search_pet(self, envget, status):
        """
        冒烟测试，基础功能
        url信息从conftest中的从envget fixture获取环境信息,返回请求的host和path
        使用参数化方法传入URL参数params进行请求
        """

        # 拼接请求为查询path
        search_url = envget + "/findByStatus"

        # 定义URL请求参数变量
        params = {
            "status": status
        }

        with allure.step("测试步骤一:发送请求"):
            # 发出查询请求
            logging.info(f"开始测试步骤一，发送请求.url:{search_url},params:{params}")
            r = requests.get(search_url, params=params)

        with allure.step("测试步骤二:断言响应结果"):
            logging.info(f"开始测试步骤二，断言结果。")
            # 状态断言
            assert r.status_code == 200
            # 业务断言
            logging.info(f'响应体信息:{r.text}')
            assert r.json() != []
            assert "id" in r.json()[0]

    @pytest.mark.错误注入测试
    @allure.feature('宠物商店')
    @allure.story('查询接口')
    @allure.title('错误测试输入错误的状态尝试查询')
    @pytest.mark.parametrize("status", ["petstatus", "12345", ""])
    def test_search_pet_failed(self, envget, status):
        """
        错误注入测试，输入错误的参数值，查询无结果返回。
        url信息从conftest中的从envget fixture获取环境信息,返回请求的host和path
        使用参数化方法传入URL参数params进行请求
        """

        # 拼接请求为查询path
        search_url = envget + "/findByStatus"

        # 定义URL请求参数变量
        params = {
            "status": status
        }

        with allure.step("测试步骤一:发送请求"):
            # 发出查询请求
            logging.info(f"开始测试步骤一，发送请求.url:{search_url},params:{params}")
            r = requests.get(search_url, params=params)

        with allure.step("测试步骤二:断言响应结果"):
            logging.info(f"开始测试步骤二，断言结果。")
            # 状态断言
            assert r.status_code == 200
            # 业务断言
            logging.info(f'响应体信息:{r.text}')
            assert r.json() == []

    @pytest.mark.空参数测试
    @allure.feature('宠物商店')
    @allure.story('查询接口')
    @allure.title('查询接口空参数测试')
    def test_search_pet_none(self, envget):
        """
        空参数测试，不传入任何参。查询无结果返回。
        url信息从conftest中的从envget fixture获取环境信息,返回请求的host和path
        """

        # 拼接请求为查询path
        search_url = envget + "/findByStatus"

        with allure.step("测试步骤一:发送请求"):
            # 发出查询请求
            logging.info(f"开始测试步骤一，发送请求.url:{search_url}")
            r = requests.get(search_url)

        with allure.step("测试步骤二:断言响应结果"):
            logging.info(f"开始测试步骤二，断言结果。")
            # 状态断言
            assert r.status_code == 200
            # 业务断言
            logging.info(f'响应体信息:{r.text}')
            assert r.json() == []

    @pytest.mark.错误参数测试
    @allure.feature('宠物商店')
    @allure.story('查询接口')
    @allure.title('查询接口错误参数测试')
    @pytest.mark.parametrize("status", ["keyword", "name", "id"])
    def test_search_pet_failed_params(self, envget, status):
        """
        错误参数测试，输入错误的参数key-value，查询无结果返回。。
        url信息从conftest中的从envget fixture获取环境信息,返回请求的host和path
        使用参数化方法传入URL参数params进行请求
        """

        # 拼接请求为查询path
        search_url = envget + "/findByStatus"

        # 定义URL请求参数变量
        params = {
            "status": status
        }

        with allure.step("测试步骤一:发送请求"):
            # 发出查询请求
            logging.info(f"开始测试步骤一，发送请求.url:{search_url},params:{params}")
            r = requests.get(search_url, params=params)

        with allure.step("测试步骤二:断言响应结果"):
            logging.info(f"开始测试步骤二，断言结果。")
            # 状态断言
            assert r.status_code == 200
            # 业务断言
            logging.info(f'响应体信息:{r.text}')
            assert r.json() == []
