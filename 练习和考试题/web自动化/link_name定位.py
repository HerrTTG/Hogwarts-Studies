import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def id_position_method():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)
    # 点击"欢迎光临测试人社区 | Powered by 霍格沃兹测试开发学社"
    driver.find_element(By.LINK_TEXT, "欢迎光临测试人社区 | Powered by 霍格沃兹测试开发学社").click()
    # 等待两秒
    time.sleep(2)


if __name__ == '__main__':
    id_position_method()
   