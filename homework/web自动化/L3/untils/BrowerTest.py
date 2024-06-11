"""
测试代码脚本
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScript:
    def setup_class(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)

    def testscript(self):
        ele = self.driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(2) > td:nth-child(1) > input")
        ele.click()
        time.sleep(3)
