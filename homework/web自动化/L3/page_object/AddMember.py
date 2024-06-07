from page_object.BasePage import BasePage


class AddMember(BasePage):

    def addmember(self):
        from page_object.AddressBook import AddressBook
        return AddressBook(self.driver)
