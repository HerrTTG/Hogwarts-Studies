import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化chromedriver
driver = webdriver.Chrome()
# 打开网站
driver.get('https://vip.ceshiren.com/#/ui_study')
# 等待一秒
time.sleep(1)

driver.implicitly_wait(3)
# 获取元素文本
print(driver.find_element(By.ID, "locate_id").text)
# 获取这个元素的name属性的值
print(driver.find_element(By.ID, "locate_id").get_attribute("name"))
