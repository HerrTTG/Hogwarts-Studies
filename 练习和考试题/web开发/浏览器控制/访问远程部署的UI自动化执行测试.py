import time
from selenium import webdriver

chrom_options = webdriver.ChromeOptions()

driver = webdriver.Remote(
    command_executor="10.88.50.185:5444",
    options=chrom_options
)
driver.get("http://www.baidu.com")
time.sleep(3)
driver.quit()
