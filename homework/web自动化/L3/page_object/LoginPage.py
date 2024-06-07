import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.BasePage import BasePage
from untils.untils import Untils


class LoginPage(BasePage):
    __homeflag = (By.CSS_SELECTOR, "#menu_index")
    __time_limit = 360

    def login(self, envinfo):
        cookie = Untils.load_cookie()

        if cookie:
            # 加cookie必须先到要加的cookie域名下
            # 所以先访问域名再加
            self.driver.get(envinfo['homeurl'])
            for c in cookie:
                self.driver.add_cookie(c)

        endtime = time.time() + LoginPage.__time_limit

        while endtime - time.time() > 0:
            self.driver.get(envinfo['homeurl'])
            try:
                if WebDriverWait(self.driver, 20, 1).until(
                        expected_conditions.visibility_of_element_located(LoginPage.__homeflag)):
                    cookie = self.driver.get_cookies()
                    Untils.save_cookie(cookie)
                    break
            except TimeoutException:
                pass
        else:
            raise '登录超时'

        from page_object.HomePage import HomePage
        return HomePage(self.driver)

    def go_home(self, envinfo):
        self.driver.get(envinfo['homeurl'])

    def goto_addressbook(self):
        from page_object.AddressBook import AddressBook
        return AddressBook(self.driver)
