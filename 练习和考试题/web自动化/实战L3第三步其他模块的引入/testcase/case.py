import allure
import logging
import pytest

from page_object import *
from untils.untils import Untils


@pytest.fixture(scope="session", autouse=True)
def get_env(request):
    """
    seesion级的fixture 并且一定要设计为自动执行。
    负责获取hook函数中添加的自定义命令行参数
    并调用工具中的读取环境信息配置文件方法，将获取到的环境信息结果赋予全局变量envinfo
    """
    myenv = request.config.getoption("--env", default='test')
    global envinfo
    envinfo = Untils.envfileload(env=myenv)
    logging.info(f'用例执行环境信息为:{envinfo}')


class Test_web():
    def setup_class(self):
        """
        实例化LoginPage界面,initdriver和浏览器
        并且调用login方法登录具体的url，赋值给主页变量
        """
        self.login = login_page.LoginPage()
        self.home = self.login.login(envinfo["baseurl"])

    def teardown_class(self):
        self.home.do_quit()

    def teardown(self):
        """
        用例方法执行后自动复位到主页
        """
        self.login.home(envinfo["homeurl"])

    @pytest.mark.parametrize('sn,name,price', [["5523231", "testhzy3", "12"]])
    def test_add(self, sn, name, price):
        """
        首页：进入商品列表
        # 点击菜单商品管理
        # 点击子菜单商品列表
        # =>>页面跳转为商品列表管理页面

        商品列表管理页面：添加商品
        # 点击添加
        # 对表单输入添加信息
        # 点击添加
        #！断言结果
        """
        with allure.step("测试步骤一:进入商品管理页面"):
            page1 = self.home.go_to_category()

        with allure.step("测试步骤二:点击添加，输入表单内容并点击上架"):
            page1.click_add().create_goods(sn, name, price)
        with allure.step("测试步骤三:断言结果，冒泡信息为创建成功"):
            assert page1.get_opertor_result('add')

    @pytest.mark.parametrize('name', ["testhzy3"])
    def test_delete(self, name):
        """
        商品列表管理页面：删除商品
        # 在搜索框输入搜索内容
        # 点击查询=>>查询到的元素
        # 对查元素结果点击删除
        #！断言结果
        """
        with allure.step("测试步骤一:进入商品管理页面"):
            page2 = self.home.go_to_category()
        with allure.step("测试步骤二:点击查询=>>查询到的元素"):
            ele = page2.click_search(name)
        with allure.step("测试步骤三:对查元素结果点击删除"):
            page2.click_delete(ele)
        with allure.step("测试步骤三:断言结果，冒泡信息为删除成功"):
            assert page2.get_opertor_result('delete')
