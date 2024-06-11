from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage


class AddressBook(BasePage):
    __addsuccessmessage = (By.XPATH, "//*[text()='保存成功']")
    __deletesuccessmessage = (By.XPATH, "//*[text()='删除成功']")
    __tr = (By.CSS_SELECTOR, "#member_list > tr")
    __deletebutton = (By.CSS_SELECTOR, ".qui_btn.ww_btn.js_delete")
    __deleteconfirm = (By.CSS_SELECTOR, "div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue")



    def get_operation_result(self, op):
        if op == 'add':
            return self.wait_element_until_visible(AddressBook.__addsuccessmessage)
        elif op == 'delete':
            return self.wait_element_until_visible(AddressBook.__deletesuccessmessage)

    def ckeck_record(self, name, phone, email):
        ##搜索所有的tr
        ##tr下的第二个td的title是name
        ##tr下的第5个td的title是phone
        ##tr下的第6个td的title是email
        eles = self.do_finds(AddressBook.__tr)
        for i in eles:
            list = self.do_finds(i, (By.CSS_SELECTOR, "td"))
            if (list[1].get_attribute("title") == name and
                    list[4].get_attribute("title") == phone):
                return i
        return False


    def deletemember(self, ele):
        # ele进来已经是匹配到要删除目标的tr元素了
        # 直接匹配ele下的第一个td内的input
        self.do_click(ele, (By.CSS_SELECTOR, "tr > td:nth-child(1) > input"))
        self.do_click(AddressBook.__deletebutton)
        self.do_click(AddressBook.__deleteconfirm)
