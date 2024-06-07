from page_object.BasePage import BasePage


class AddressBook(BasePage):
    def get_operation_result(self, op):
        return True

    def ckeck_record(self, name):
        return True

    def deletemember(self, ele):
        pass
