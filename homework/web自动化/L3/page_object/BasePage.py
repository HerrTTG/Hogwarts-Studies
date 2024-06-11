import logging
import time
from selenium import webdriver
from selenium.common import TimeoutException
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
            Untils.save_screenshot(driver, f'异常截图')
            Untils.save_page_soure(driver, f'异常源码')
            logging.info(f"异常方法,参数{args},{kwargs}")
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
        # 如果locator为空，则by必定为元组类型的元素表达式
        # 不为空则有两种可能，第一是BY+表达式解包传入
        # 第二是BY本身为元素，locator为元组表达式。需要基于元素的再次搜索。
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
        # 如果locator为空，则by必定为元组类型的元素表达式
        # 不为空则有两种可能，第一是BY+表达式解包传入
        # 第二是BY本身为元素，locator为元组表达式。需要基于元素的再次搜索。
        if locator:
            if isinstance(by, WebElement):
                # 判断By对象是属于元素类的
                # 返回By元素搜索其下的locator
                return by.find_elements(*locator)
            else:
                return self.driver.find_elements(by, locator)
        else:
            ##如果没穿locator 则解包by 说明传入的是一个元组
            return self.driver.find_elements(*by)

    @ui_exception_record
    def do_send(self, vaule, by=By.ID, locator=None):
        # 如果locator为空，则by必定为元组类型的元素表达式
        # 不为空则有两种可能，第一是BY+表达式解包传入
        # 第二是BY本身为元素，locator为元组表达式。需要基于元素的再次搜索。
        if locator:
            if isinstance(by, WebElement):
                # 判断By对象是属于元素类的
                # 返回By元素搜索其下的locator
                ele = self.do_find(by, locator)
            else:
                ele = self.do_find((by, locator))
        else:
            ele = self.do_find(*by)

        ele.clear()
        ele.send_keys(vaule)
        time.sleep(1)

    @ui_exception_record
    def do_click(self, by=By.ID, locator=None):
        # 如果locator为空，则by必定为元组类型的元素表达式
        # 不为空则有两种可能，第一是BY+表达式解包传入
        # 第二是BY本身为元素，locator为元组表达式。需要基于元素的再次搜索。
        if locator:
            if isinstance(by, WebElement):
                # 判断By对象是属于元素类的
                self.do_find(by, locator).click()
            else:
                self.wait_element_until_visible((by, locator)).click()
        else:
            self.wait_element_until_visible(by).click()
        time.sleep(1)

    @ui_exception_record
    def wait_element_until_visible(self, locator: tuple[str, str], timeout=5):
        return WebDriverWait(self.driver, timeout, 1).until(
            expected_conditions.visibility_of_element_located(locator))

    @ui_exception_record
    def scroll_to_element_click(self, driver, ele):
        ActionChains(driver).scroll_to_element(ele).click(ele).perform()

    def do_quit(self):
        self.driver.quit()

    def login_check(self, timeout, locator: tuple[str, str], cookie=False, message=''):
        ##登录检查
        # 页面跳转后，检查指定元素locator来判断是否跳转成功
        ##分为无需保存cookie和需要保存cookie的
        #等待失败后弹提醒

        try:
            if WebDriverWait(self.driver, timeout, 1).until(
                    expected_conditions.visibility_of_element_located(locator)) and cookie is True:
                cookie = self.driver.get_cookies()
                Untils.save_cookie(cookie)
                return True
            elif WebDriverWait(self.driver, timeout, 1).until(
                    expected_conditions.visibility_of_element_located(locator)):
                return True
        except TimeoutException:
            self.show_alert(message)
            return False

    def show_alert(self, message):
        ##设置弹窗提醒
        self.driver.execute_script(f"window.alert('{message}')")
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.refresh()
