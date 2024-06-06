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
            # 如果子菜单已经展示，说明可以直接点击子菜单。
            # 如果在去点击主菜单后再尝试点子菜单，会因为主菜单点后将子菜单收起而无法点击
            self.do_click(HomePage.__categorysub_menu)
        else:
            # 先点主菜单
            self.do_click(HomePage.__category)
            # 再点击子菜单商品列表
            self.do_click(HomePage.__categorysub_menu)

        # =>>页面跳转为商品列表管理页面
        Untils.save_screenshot(self.driver, '转为商品列表管理页面')
        from page_object.category_page import CategoryPage
        return CategoryPage(self.driver)
