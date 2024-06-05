from selenium import webdriver
from selenium.webdriver.common.by import By


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

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

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

    def do_click(self, by=By.ID, locator=None):
        if locator:
            self.do_find(by, locator).click()
        else:
            self.do_find(*by).click()

    def do_quit(self):
        self.driver.quit()
