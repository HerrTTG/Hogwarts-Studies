"""
=====Python版本=====
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ceshiren():
    # 切换成 windows 就会报错
    options = webdriver.ChromeOptions()
    options.platform_name = 'Windows 10'

    driver = webdriver.Remote(
        command_executor="https://selenium-node.hogwarts.ceshiren.com/ui#",
        keep_alive=True,
        options=options)

    driver.implicitly_wait(5)
    driver.get("https://ceshiren.com/")
    # 输入框输入搜索内容[霍格沃兹测试学院]
    text = driver.find_element(By.CSS_SELECTOR, ".login-button").text
    # 点击搜索按钮
    print(text)
    time.sleep(30)
    driver.quit()
