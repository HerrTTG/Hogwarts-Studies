# --allure-severities normal,blocker
import allure


@allure.severity(allure.severity_level.BLOCKER)
class Testlogin():
    @allure.issue('bug', "bug管理系统")
    def testcase1(self):
        """
        我是一个用例描述
        """
        assert True

    def testcase2(self):
        assert False


@allure.severity(allure.severity_level.TRIVIAL)
class Testpayment():
    def testcase1(self):
        assert True

    def testcase2(self):
        assert False
