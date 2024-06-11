import time
from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage
from untils.untils import Untils


class HomePage(BasePage):
    __addmemberbutton = (By.XPATH, "//*[text()='添加成员']")

    def click_addmember(self):
        self.do_click(HomePage.__addmemberbutton)
        time.sleep(1)
        Untils.save_screenshot(self.driver, message="进入添加成员")
        from page_object.AddMember import AddMember
        return AddMember(self.driver)
