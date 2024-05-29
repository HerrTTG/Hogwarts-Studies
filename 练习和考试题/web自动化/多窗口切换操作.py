# -*- coding: UTF-8 -*-
# author: joker
# perject:web_python
# name:test_window.py
# date:2023/8/9
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestWindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 点击后会生成2个窗口
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        # 将所有的窗口的句柄生成列表
        windows = self.driver.window_handles
        # 利用切换窗口方法，输入窗口的句柄切换到最后一个窗口
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("13800000000")

        # 切回原来的窗口
        self.driver.switch_to.window(windows[0])

        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()

        sleep(3)
