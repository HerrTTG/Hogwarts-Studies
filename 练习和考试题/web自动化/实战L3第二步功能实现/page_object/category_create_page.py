from page_object.BasePage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CategoryCreatePage(BasePage):
    __goodsnumber = (By.CSS_SELECTOR, "label[for='goodsSn'] + div.el-form-item__content > div > input")
    __goodsname = (By.CSS_SELECTOR, "label[for='name'] + div.el-form-item__content > div > input")
    __goodsprice = (By.CSS_SELECTOR, "label[for='counterPrice'] + div.el-form-item__content > div > input")
    __addbutton = (By.CSS_SELECTOR, ".op-container > button:nth-child(2)")

    def create_category(self, sn, name, price):
        # 添加商品表单：添加商品
        # 对表单进行输入
        self.do_send(sn, CategoryCreatePage.__goodsnumber)
        self.do_send(name, CategoryCreatePage.__goodsname)
        self.do_send(price, CategoryCreatePage.__goodsprice)

        # 滑动页面并点击添加
        ele1 = self.do_find(CategoryCreatePage.__addbutton)
        ActionChains(self.driver).scroll_to_element(ele1).click(ele1).perform()
