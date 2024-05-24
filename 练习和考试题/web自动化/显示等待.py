import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # WebDriverWait(driver,最长等待时间)
    # until(method)
    # expected_conditions.element_to_be_clickable((选择器,元素))

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#success_btn')))

    driver.find_element(By.CSS_SELECTOR, "#success_btn").click()
    time.sleep(3)


if __name__ == '__main__':
    wait_until()
