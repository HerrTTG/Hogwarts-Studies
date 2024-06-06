from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage
from untils.untils import Untils


class CategoryCreatePage(BasePage):
    __goodsnumber = (By.CSS_SELECTOR, "label[for='goodsSn'] + div.el-form-item__content > div > input")
    __goodsname = (By.CSS_SELECTOR, "label[for='name'] + div.el-form-item__content > div > input")
    __goodsprice = (By.CSS_SELECTOR, "label[for='counterPrice'] + div.el-form-item__content > div > input")
    __addbutton = (By.CSS_SELECTOR, ".op-container > button:nth-child(2)")

    def create_goods(self, sn, name, price):
        # 添加商品表单：添加商品
        # 对表单进行输入
        # 测试车次测吃啥在试一次
        self.do_send(sn, CategoryCreatePage.__goodsnumber)
        self.do_send(name, CategoryCreatePage.__goodsname)
        self.do_send(price, CategoryCreatePage.__goodsprice)

        Untils.save_screenshot(self.driver, '对表单输入')
        # 滑动页面并点击添加
        ele1 = self.do_find(CategoryCreatePage.__addbutton)
        self.scroll_to_element_click(self.driver, ele1)
