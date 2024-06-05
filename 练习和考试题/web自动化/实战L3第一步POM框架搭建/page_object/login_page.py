from page_object.BasePage import BasePage


class LoginPage(BasePage):
    def login(self, url):
        # 登录页面：用户输入信息登录
        # 访问首页
        # 输入用户名
        # 输入密码
        # 点击登录

        # =>>页面跳转为首页
        from page_object.home_page import HomePage
        # login的时候需要初始化一个driver来打开页面 所以login被实例化的时候不需要传入driver
        # 但是后续的页面如果不希望打开新的页面进行执行，就需要传入现有的driver
        return HomePage(self.driver)

    def home(self, homeurl):
        ## 返回home页面
        ## 用于用例和用例之间的初始化
        ## 访问home主页
        self.driver.get(url=homeurl)

        from page_object.home_page import HomePage
        return HomePage(self.driver)
