import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化chromedriver
driver = webdriver.Chrome()
# 打开网站
driver.get('http://www.baidu.com')
# 等待一秒
time.sleep(1)

# 点击百度搜索框
driver.find_element(By.ID, "kw").click()
time.sleep(2)
# 输入"霍格沃兹测试开发"
driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试开发")
time.sleep(2)
# 清空搜索框中信息
driver.find_element(By.ID, "kw").clear()
time.sleep(2)
