import logging
import pytest

from page_object import *
from untils.untils import Untils


@pytest.fixture(scope="session", autouse=True)
def get_env(request):
    myenv = request.config.getoption("--env", default='test')
    global envinfo
    envinfo = Untils.envfileload(env=myenv)
    logging.info(f'用例执行环境信息为:{envinfo}')


class Test_web():
    def setup_class(self):
        self.login = login_page.LoginPage()
        self.home = self.login.login(envinfo["baseurl"])

    def teardown_class(self):
        self.home.do_quit()

    def teardown(self):
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
        page1 = self.home.go_to_category()
        page1.click_add().create_goods(sn, name, price)
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
        page2 = self.home.go_to_category()
        ele = page2.click_search(name)
        page2.click_delete(ele)
        assert page2.get_opertor_result('delete')
