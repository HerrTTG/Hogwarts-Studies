import time
from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage
from untils.untils import Untils


class LoginPage(BasePage):
    __inputuser = (By.CSS_SELECTOR, 'input[name="username"]')
    __inputpassword = (By.CSS_SELECTOR, 'input[name="password"]')
    __loginsubmit = (By.TAG_NAME, "button")

    def login(self, baseurl):
        # 登录页面：用户输入信息登录
        self.driver.get(baseurl)
        # 输入用户名
        # 输入密码
        self.do_send('manage', LoginPage.__inputuser)
        self.do_send('manage123', LoginPage.__inputpassword)
        # 点击登录
        self.do_click(LoginPage.__loginsubmit)

        # =>>页面对象跳转为首页
        Untils.save_screenshot(self.driver, '登录')
        from page_object.home_page import HomePage
        # login的时候需要初始化一个driver来打开页面 所以login被实例化的时候不需要传入driver
        # 但是后续的页面如果不希望打开新的页面进行执行，就需要传入现有的driver
        return HomePage(self.driver)

    def home(self, homeurl):
        ## 返回home页面
        ## 用于用例和用例之间的初始化
        ## 访问home主页
        self.driver.get(url=homeurl)
        time.sleep(1)

        Untils.save_screenshot(self.driver, '返回主页')
        from page_object.home_page import HomePage
        return HomePage(self.driver)
