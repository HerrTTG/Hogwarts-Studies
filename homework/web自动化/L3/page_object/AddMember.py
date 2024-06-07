from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage


class AddMember(BasePage):
    # save按键有两个
    __savebutton = (By.XPATH, "//*[text()='保存']")
    __inputname = (By.CSS_SELECTOR, "input#username")
    __inputid = (By.CSS_SELECTOR, "input#memberAdd_acctid")
    __inputphone = (By.CSS_SELECTOR, "input#memberAdd_phone")
    __inputemail = (By.CSS_SELECTOR, "input#memberAdd_mail")

    def addmember(self, name, acctid, phone, email):
        self.do_send(name, AddMember.__inputname)
        self.do_send(acctid, AddMember.__inputid)
        self.do_send(phone, AddMember.__inputphone)
        self.do_send(email, AddMember.__inputemail)

        self.do_click(AddMember.__savebutton)

        from page_object.AddressBook import AddressBook
        return AddressBook(self.driver)
