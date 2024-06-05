from page_object.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    __category = (By.XPATH, "//*[text()='商品管理']")
    __categorysub_menu = (By.XPATH, "//*[text()='商品列表']")

    def go_to_category(self):
        # 首页：进入商品列表
        # 点击菜单商品管理
        if self.driver.find_element(*HomePage.__categorysub_menu).is_displayed():
            # 点击子菜单商品列表
            self.do_click(HomePage.__categorysub_menu)
        else:
            self.do_click(HomePage.__category)
            # 点击子菜单商品列表
            self.do_click(HomePage.__categorysub_menu)
        # =>>页面跳转为商品列表管理页面
        from page_object.category_page import CategoryPage
        return CategoryPage(self.driver)
