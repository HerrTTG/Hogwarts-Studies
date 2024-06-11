import time
from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage
from untils.untils import Untils


class LoginPage(BasePage):
    __homeflag = (By.XPATH, "//*[text()='首页']")
    __addressflag = (By.XPATH, "//*[text()='通讯录']")
    __time_limit_max = 360
    __time_limit = 20

    def login(self, envinfo, noretry=True):
        """
        # 初始化后判断是否存在cookie文件
        # 存在=>读取cookie文件
        # 将cookie文件信息导入driver
        # 直接尝试访问首页
        # 设置最大等待时间和元素等待时间
        # 判断首页元素是否展示
        # =>存在 保存cookie信息，退出循环。
        # =>不存在 等待下一次循环直到最大等待时间结束还未找到首页元素则抛出异常
        """
        cookie = Untils.load_cookie()

        if cookie and noretry is True:
            ## noretry 来判断是否为下一个用例跳转。
            # 下一个用例跳转如果直接访问失败，说明cookie失效，所以不直接使用cookie
            self.driver.get(envinfo['homeurl'])
            # 加cookie必须先到要加的cookie域名下
            # 所以先访问域名再加
            for c in cookie:
                self.driver.add_cookie(c)

        endtime = time.time() + LoginPage.__time_limit_max

        self.driver.get(envinfo['homeurl'])

        # 设置最大等待时间，进入循环判断页面跳转成功与否
        while endtime - time.time() > 0:
            if self.login_check(LoginPage.__time_limit, LoginPage.__homeflag,
                                cookie=True, message="请扫码登录"):
                break
        else:
            self.show_alert(message="window.alert('登录超时')")
            raise '登录超时'

        Untils.save_screenshot(self.driver, message="登录成功")
        from page_object.HomePage import HomePage
        return HomePage(self.driver)

    def go_home(self, envinfo):
        self.driver.get(envinfo['homeurl'])
        if self.login_check(5, LoginPage.__homeflag,
                            cookie=False, message="请重新登录"):

            Untils.save_screenshot(self.driver, message="返回主页成功")
            from page_object.HomePage import HomePage
            return HomePage(self.driver)
        else:
            self.login(envinfo, noretry=False)


    def goto_addressbook(self):

        self.do_click(LoginPage.__addressflag)
        Untils.save_screenshot(self.driver, message="进入通讯录")
        from page_object.AddressBook import AddressBook
        return AddressBook(self.driver)
