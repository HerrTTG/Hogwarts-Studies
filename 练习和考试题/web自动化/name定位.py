import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def name_position_method():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.baidu.com')
    # 等待一秒
    time.sleep(1)
    # 点击更多
    driver.find_element(By.NAME, "tj_briicon").click()
    # 等待两秒
    time.sleep(2)


if __name__ == '__main__':
    name_position_method()
