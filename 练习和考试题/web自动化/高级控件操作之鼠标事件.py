import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestKeyBoardDemo:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_double_click(self):
        # 演练环境
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        ele = self.driver.find_element(By.ID, "primary_btn")
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(2)

    def test_drag_and_drop(self):
        """
        拖拽控件
        """
        # 演练环境
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        # 定位需要拖拽的元素item_left
        # 定位要拖到的位置元素item_right
        item_left = self.driver.find_element(By.CSS_SELECTOR, '#item1')
        item_right = self.driver.find_element(By.CSS_SELECTOR, '#item3')
        # drag_and_drop进行拖拽
        ActionChains(self.driver).drag_and_drop(item_left, item_right).perform()
        time.sleep(5)

    def test_move_to_element(self):
        """
        有些元素（下拉框元素），需要先悬浮鼠标到对应控件上 才会显示。才能被点击。move_to_element 就是用来模拟鼠标移动到某元素上。
        """
        # 演练环境
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        time.sleep(2)
        # 定位选择框
        title = self.driver.find_element(By.CSS_SELECTOR, '.title')
        # 悬浮岛选择框上，使选项显露出来
        ActionChains(self.driver).move_to_element(title).perform()
        # 点击其中一个元素
        options = self.driver.find_element(By.CSS_SELECTOR, '.options>div:nth-child(1)')
        ActionChains(self.driver).click(options).perform()
        time.sleep(5)
