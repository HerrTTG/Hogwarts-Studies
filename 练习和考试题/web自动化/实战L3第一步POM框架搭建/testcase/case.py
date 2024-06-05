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

    def teardown_method(self):
        self.login.home(envinfo["homeurl"])

    def teardown_class(self):
        self.login.do_quit()

    def test_add(self):
        page1 = self.home.go_to_category()
        page1.click_add().create_category()
        result = page1.get_opertor_result()
        print(result)

    def test_delete(self):
        page2 = self.home.go_to_category()
        ele = page2.click_search()
        page2.click_delete(ele)
        result = page2.get_opertor_result()
        print(result)
