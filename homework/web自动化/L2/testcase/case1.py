import random
import sys

sys.path.append('..\\..\\L2')

import pytest
import allure
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from untils.untils import Untils


@pytest.fixture(scope="class")
def get_env(request):
    myenv = request.config.getoption("--env", default='test')
    envinfo = Untils.envfileload(env=myenv)
    logging.info(f'用例执行环境信息为:{envinfo}')
    return envinfo


class Test_web():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("search", Untils.get_testdata()['datas'])
    def test_case1(self, search, get_env):
        id = random.randint(1, 9999)
        # 动态更新用例标题，可以参与到用例执行中去增加当前用例的标题名
        allure.dynamic.title(f"用例id:{id}")
        logging.info(f"用例id:{id}")

        # Test name: 测试人论坛搜索
        # Step # | name | target | value
        # 1 | open url
        self.driver.get(get_env['baseurl'])
        Untils.save_screenshot(self.driver, id=id, message='open url')

        # 2 | click | 搜索按钮
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".d-icon-search"))).click()

        # 3 | click | 高级搜索按钮
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".d-icon-sliders-h"))).click()

        # 4 | click | 输入搜索关键字
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//*[text()='高级筛选器']")))
        except:
            logging.info(f"用例id:{id} 跳转高级搜索失败")
            raise AssertionError
        else:
            Untils.save_screenshot(self.driver, id=id, message='高级搜索')
            Untils.save_page_soure(self.driver.page_source, id=id, message='高级搜索')

        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='输入搜索关键字']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='输入搜索关键字']").clear()

        # 5 | type | css=[aria-label='输入搜索关键字']|
        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='输入搜索关键字']").send_keys(search)
        logging.info(f"用例id:{id} 输入搜索关键字：{search}")
        Untils.save_screenshot(self.driver, id=id, message='输入截图')

        # 6 | click | 搜索
        self.driver.find_element(By.CSS_SELECTOR, "div.search-bar > button ").click()

        # 7 | finds | 标题和高亮
        ls_t = self.driver.find_elements(By.CSS_SELECTOR, '.topic-title')
        ls_h = self.driver.find_elements(By.CSS_SELECTOR, '.search-highlight')

        # 8 | assert|
        try:
            assert search in ls_t[0].text or search in ls_h[0].text
        except:
            print('查询结果失败')
            Untils.save_screenshot(self.driver, id=id, message='失败结果')
            Untils.save_page_soure(self.driver.page_source, id=id, message='失败结果')
            logging.info(f"用例id:{id} 鉴权失败所搜索结果与页面结果不符")
            logging.info(f"用例id:{id} 第一个标题：{ls_t[0].text}")
            logging.info(f"用例id:{id} 高亮内容：{ls_h[0].text}")
            raise AssertionError
        else:
            print(ls_t[0].text)
            logging.info(f"用例id:{id} 鉴权成功")
            logging.info(f"用例id:{id} 第一个标题：{ls_t[0].text}")
            logging.info(f"用例id:{id} 高亮内容：{ls_h[0].text}")
            Untils.save_screenshot(self.driver, id=id, message='成功结果')
            Untils.save_page_soure(self.driver.page_source, id=id, message='成功结果')
