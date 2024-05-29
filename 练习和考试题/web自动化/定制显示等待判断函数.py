"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 如果没有完全掌握也没有关系，这部分对代码的功底要求较高
# 输入一： 点击的目标按钮 输入二： 下一个页面的某个元素


def test_case1():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")

    # 问题： 使用官方提供的expected condition 已经无法满足需求
    # 解决方案： 自己封装期望条件
    # 期望条件的设计： 需求： 一直点击按钮，直到下一个页面出现为止
    # until 中传入自己封装的判断函数

    result = WebDriverWait(driver, 10, 1).until(
        muliti_click(
            (By.ID, "primary_btn"),
            (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")
        ))

    try:
        assert result.text == '该弹框点击两次后才会弹出'
    except:
        raise AssertionError
    else:
        time.sleep(3)


def muliti_click(target_element, next_element):
    # muliti_click是一个闭包函数
    # 在until函数传参时，首次被调用muliti_click(
    #             (By.ID, "primary_btn"),
    #             (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")
    #         )
    # 将两个实参传入，并返回内置函数_inner为对象。
    # 在until 函数的运行中
    #  value = method(self._driver)
    # 此时的method就等于函数的对象，即_inner
    # value = _inner(self._driver)
    # 在_inner中利用的闭包的特性，内置函数可以用外层函数的局部变量，即muliti_click传入的两个参数。

    def _inner(driver):
        # 尝试点击
        driver.find_element(*target_element).click()

        # 直接使用return来find期望结果元素
        # 第一种结果为找到, return 的内容为webelement 对象  True
        # 第二种结果为未找到， driver.find_element(*next_element) 代码报错
        # 但是被 until中的异常捕获逻辑捕获异常。继续循环
        # 直到timeout时间用尽，如若没有一次return的是 True。则等待失败 代码报错
        return driver.find_element(*next_element)

    return _inner


if __name__ == '__main__':
    test_case1()
