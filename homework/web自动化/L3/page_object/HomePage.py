from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage


class HomePage(BasePage):
    __addmemberbutton = (By.XPATH, "//*[text()='添加成员']")

    def click_addmember(self):
        self.do_click(HomePage.__addmemberbutton)

        from page_object.AddMember import AddMember
        return AddMember(self.driver)
