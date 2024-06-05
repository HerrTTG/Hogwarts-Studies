from page_object.BasePage import BasePage


class HomePage(BasePage):
    def go_to_category(self):
        # 首页：进入商品列表
        # 点击菜单商品管理
        # 点击子菜单商品列表

        # =>>页面跳转为商品列表管理页面
        from page_object.category_page import CategoryPage
        return CategoryPage(self.driver)
