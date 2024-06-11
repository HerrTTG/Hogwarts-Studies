import logging
import pytest
import time

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


global testdata
testdata = Untils.get_testdata()

class Test_web():
    def setup_class(self):
        self.home = LoginPage.LoginPage()

    def teardown_class(self):
        self.home.do_quit()

    def teardown(self):
        """
        用例方法执行后自动复位到主页
        """
        self.home.go_home(envinfo)

    @pytest.mark.parametrize('name,id,phone,email', testdata["case1"])
    def testcase1(self, name, id, phone, email):
        result = self.home.login(envinfo).click_addmember().addmember(name, id, phone, email)
        assert result.get_operation_result("add")
        time.sleep(5)
        assert result.ckeck_record(name, phone, email)

    @pytest.mark.parametrize('name,id,phone,email', testdata["case1"])
    def testcase2(self, name, id, phone, email):
        addressbook = self.home.goto_addressbook()
        ele = addressbook.ckeck_record(name, phone, email)
        addressbook.deletemember(ele)
        assert addressbook.get_operation_result('delete')
