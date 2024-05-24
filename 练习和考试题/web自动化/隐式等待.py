import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def wait_sleep():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错

    # 添加隐式等待，整个driver都会生效
    driver.implicitly_wait(3)

    # 针对查找元素这个动作 添加隐式等待后，会轮询查找。每0.5秒一次。等待多久由函数入参决定。
    # 等待时间到，但轮询结果依然为空才抛出异常
    driver.find_element(By.XPATH, "//*[text()='个人中心']")
    time.sleep(3)


if __name__ == '__main__':
    wait_sleep()
