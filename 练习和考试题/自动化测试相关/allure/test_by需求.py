# pytest 测试driver.py --allure-epics=case1
# pytest 测试driver.py --allure-features=func1
# pytest 测试driver.py --allure-features=func2
# pytest 测试driver.py --allure-stories=success
# pytest 测试driver.py --allure-stories=faild
import allure


@allure.epic('case1')
@allure.feature('func1')
class Testlogin():
    @allure.issue('bug', "bug管理系统")
    @allure.story('success')
    def testcase1(self):
        """
        我是一个用例描述
        """
        assert True

    @allure.story('faild')
    def testcase2(self):
        assert False


@allure.epic('case1')
@allure.feature('func2')
class Testpayment():
    @allure.story('success')
    def testcase1(self):
        assert True

    @allure.story('faild')
    def testcase2(self):
        assert False
