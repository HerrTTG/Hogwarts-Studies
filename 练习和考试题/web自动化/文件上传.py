import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestKeyBoardDemo:
    """
    未实现
    """

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_input_file_by_window(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element(By.CSS_SELECTOR, ".img-upload-icon_y6ZWd").click()
        self.driver.find_element(By.CSS_SELECTOR, ".upload-btn_3JqrF").click()
        WebDriverWait(self.driver, 5, 0.5).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys("E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\图像处理\picframe59.png")
        alert.accept()
        time.sleep()
