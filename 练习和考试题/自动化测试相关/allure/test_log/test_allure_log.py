import allure
import sys

sys.path.append('./')
from log_until import logger


@allure.feature("功能模块2")
class TestWithLogger:
    @allure.story("子功能1")
    @allure.title("用例1")
    def test_case1(self):
        logger.info("用例1的 info 级别的日志")
        logger.debug("用例1的 debug 级别的日志")
        logger.warning("用例1的 warning 级别的日志")
        logger.error("用例1的 error 级别的日志")
        logger.fatal("用例1的  fatal 级别的日志")
