import time
from selenium import webdriver

driver = webdriver.Chrome()

# 打开浏览器
driver.get('https://www.baidu.com')
time.sleep(3)

# 刷新浏览器
driver.refresh()
time.sleep(3)

# 退回
driver.back()
time.sleep(3)

# 最大化
driver.maximize_window()
time.sleep(3)

# 最大化
driver.minimize_window()
time.sleep(3)
