import allure
import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_web():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        if os.path.exists("./report/images") is False: os.makedirs("./report/images")

        self.driver.get('http://litemall.hogwarts.ceshiren.com/#/dashboard')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys('manage')

        self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('manage123')
        self.driver.find_element(By.TAG_NAME, "button").click()

    def teardown_class(self):
        self.driver.quit()
        # 删除测试数据

    def until(self):
        return time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime())

    @pytest.mark.parametrize('sn,name,price', [["5523231", "testhzy3", "12"]])
    def testcase1(self, sn, name, price):
        ## 唯一名称可以用XPATH text的方法寻找
        self.driver.find_element(
            By.XPATH, "//*[text()='商品管理']").click()
        self.driver.find_element(
            By.XPATH, "//*[text()='商品列表']").click()
        self.driver.find_element(
            By.XPATH, "//*[text()='添加']").click()

        self.driver.find_element(By.CSS_SELECTOR, "label[for='goodsSn'] + div.el-form-item__content"). \
            find_element(By.CSS_SELECTOR, "input").send_keys(sn)

        self.driver.find_element(By.CSS_SELECTOR, "label[for='name'] + div.el-form-item__content"). \
            find_element(By.CSS_SELECTOR, "input ").send_keys(name)

        self.driver.find_element(By.CSS_SELECTOR, "label[for='counterPrice'] + div.el-form-item__content"). \
            find_element(By.CSS_SELECTOR, "input ").send_keys(price)

        ele1 = self.driver.find_element(By.CSS_SELECTOR, ".op-container > button:nth-child(2)")

        ActionChains(self.driver).scroll_to_element(ele1).click(ele1).perform()

        try:
            WebDriverWait(self.driver, 5, 1).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='创建成功']")))
        except:
            raise AssertionError
        else:
            timestamp = self.until()
            file = f"./report/images/screenshot_{timestamp}.png"
            self.driver.save_screenshot(file)
            allure.attach.file(file, name="pic1",
                               attachment_type=allure.attachment_type.PNG)
            time.sleep(5)
