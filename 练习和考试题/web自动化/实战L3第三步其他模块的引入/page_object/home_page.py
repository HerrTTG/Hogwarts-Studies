from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage
from untils.untils import Untils


class HomePage(BasePage):
    __category = (By.XPATH, "//*[text()='商品管理']")
    __categorysub_menu = (By.XPATH, "//*[text()='商品列表']")

    def go_to_category(self):
        # 首页：进入商品列表
        # 点击菜单商品管理
        if self.do_find(HomePage.__categorysub_menu).is_displayed():
            # 点击子菜单商品列表
            self.do_click(HomePage.__categorysub_menu)
        else:
            self.do_click(HomePage.__category)
            # 点击子菜单商品列表
            self.do_click(HomePage.__categorysub_menu)
        # =>>页面跳转为商品列表管理页面
        Untils.save_screenshot(self.driver, '转为商品列表管理页面')
        from page_object.category_page import CategoryPage
        return CategoryPage(self.driver)
