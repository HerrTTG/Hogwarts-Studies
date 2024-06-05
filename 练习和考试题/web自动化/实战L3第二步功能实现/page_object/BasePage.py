import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, base_driver=None):
        """
        driver初始化
        判断是否传入driver
        """
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

    ## selenium API方法封装

    def do_find(self, by=By.ID, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            ##如果没穿locator 则解包by 说明传入的是一个元组
            return self.driver.find_element(*by)
        # return "元素"

    def do_finds(self, by=By.ID, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            ##如果没穿locator 则解包by 说明传入的是一个元组
            return self.driver.find_elements(*by)

    def do_send(self, vaule, by=By.ID, locator=None):
        if locator:
            ele = self.do_find(by, locator)
        else:
            ele = self.do_find(*by)

        ele.clear()
        ele.send_keys(vaule)
        time.sleep(1)

    def do_click(self, by=By.ID, locator=None):
        if locator:
            WebDriverWait(self.driver, 5, 1).until(
                expected_conditions.visibility_of_element_located((by, locator))).click()
        else:
            WebDriverWait(self.driver, 5, 1).until(
                expected_conditions.visibility_of_element_located(by)).click()
        time.sleep(1)

    def do_quit(self):
        self.driver.quit()
