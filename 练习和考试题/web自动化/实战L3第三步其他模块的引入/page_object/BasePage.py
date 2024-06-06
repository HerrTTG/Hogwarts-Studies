import logging
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from untils.untils import Untils


def ui_exception_record(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            driver = args[0].driver
            Untils.save_screenshot(driver, f'异常截图，方法:{func}')
            Untils.save_page_soure(driver, f'异常源码，方法:{func}')
            logging.info(f"异常方法为{func},参数{args},{kwargs}")
        raise Exception

    return inner


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

    @ui_exception_record
    def do_find(self, by=By.ID, locator=None):
        if locator:
            if isinstance(by, WebElement):
                return by.find_element(*locator)
            else:
                return self.driver.find_element(by, locator)
        else:
            ##如果没穿locator 则解包by 说明传入的是一个元组
            return self.driver.find_element(*by)
        # return "元素"

    @ui_exception_record
    def do_finds(self, by=By.ID, locator=None):
        if locator:
            if isinstance(by, WebElement):
                return by.find_elements(*locator)
            else:
                return self.driver.find_elements(by, locator)
        else:
            ##如果没穿locator 则解包by 说明传入的是一个元组
            return self.driver.find_elements(*by)

    @ui_exception_record
    def do_send(self, vaule, by=By.ID, locator=None):
        if locator:
            ele = self.do_find(by, locator)
        else:
            ele = self.do_find(*by)

        ele.clear()
        ele.send_keys(vaule)
        time.sleep(1)

    @ui_exception_record
    def do_click(self, by=By.ID, locator=None):
        if locator:
            if isinstance(by, WebElement):
                self.do_find(by, locator).click()
            else:
                self.wait_element_until_visible((by, locator)).click()
        else:
            self.wait_element_until_visible(by).click()
        time.sleep(1)

    @ui_exception_record
    def wait_element_until_visible(self, locator: tuple[str, str]):
        return WebDriverWait(self.driver, 5, 1).until(
            expected_conditions.visibility_of_element_located(locator))

    @ui_exception_record
    def scroll_to_element_click(self, driver, ele):
        ActionChains(driver).scroll_to_element(ele).click(ele).perform()

    def do_quit(self):
        self.driver.quit()
