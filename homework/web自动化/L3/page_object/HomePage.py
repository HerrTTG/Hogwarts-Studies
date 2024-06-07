from page_object.BasePage import BasePage


class HomePage(BasePage):
    def click_add(self):
        from page_object.AddMember import AddMember
        return AddMember(self.driver)
