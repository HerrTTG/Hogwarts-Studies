import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestKeyBoardDemo:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_scoll_to_element(self):
        """
        滚轮滚动到指定元素
        """
        # 演练环境
        self.driver.get("https://ceshiren.com/")
        # selenium 4.2 之后才提供这个方法
        ele = self.driver.find_element \
            (By.XPATH, "//*[text()='怎么写高可用集群部署的测试方案？']")
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(5)

    def test_scroll_to_amount(self):
        """
        滚动到指定坐标
        """
        # 演练环境
        self.driver.get("https://ceshiren.com/")
        # selenium4.2 之后才提供这个方法
        ActionChains(self.driver).scroll_by_amount(0, 10000).perform()
        time.sleep(5)
