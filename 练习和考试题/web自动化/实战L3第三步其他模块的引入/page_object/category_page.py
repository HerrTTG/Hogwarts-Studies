from selenium.webdriver.common.by import By

from page_object.BasePage import BasePage
from untils.untils import Untils


class CategoryPage(BasePage):
    __serchbyname = (By.CSS_SELECTOR, "input[placeholder=请输入商品名称]")
    __serchbutton = (By.CSS_SELECTOR, "div.filter-container >button")
    __serchrow = (By.CSS_SELECTOR, '.el-table__row')
    __rowname = (By.CSS_SELECTOR, 'tr > td:nth-child(3)')
    __deletebutton = (By.CSS_SELECTOR, "button.el-button.el-button--danger.el-button--mini")
    __addbutton = (By.XPATH, "//*[text()='添加']")
    __addmessage = (By.XPATH, "//*[text()='创建成功']")
    __deletemessage = (By.XPATH, "//*[text()='删除成功']")

    def click_add(self):
        # 商品列表管理页面：点击添加
        # 点击添加
        self.do_click(CategoryPage.__addbutton)
        # =>>跳转添加商品表单
        Untils.save_screenshot(self.driver, '跳转添加商品表单页面')
        from page_object.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    def click_search(self, seach_name):
        # 商品列表管理页面：点击查询
        # 输入框输入搜索内容
        self.do_send(seach_name, CategoryPage.__serchbyname)
        Untils.save_screenshot(self.driver, '输入搜索内容')
        # 点击查询
        self.do_click(CategoryPage.__serchbutton)
        Untils.save_screenshot(self.driver, '查询结果')
        # 搜索所有结果列
        eles = self.do_finds(CategoryPage.__serchrow)
        for i in eles:
            # 对每一行校验第三列name是否为输入的查询关键字 返回row
            if self.do_find(i, CategoryPage.__rowname). \
                    get_attribute('innerText') == seach_name:
                return i
        else:
            return False

    def click_delete(self, row):
        # 商品列表管理页面：删除商品
        # 获取符合结果的数据的元素ele所在的位置的delete元素位置
        # 寻找row内的删除按钮
        # 点击删除按钮
        self.do_click(row, CategoryPage.__deletebutton)

    def get_opertor_result(self, op):
        if op == 'add':
            # 冒泡信息获取
            if self.wait_element_until_visible(CategoryPage.__addmessage):
                Untils.save_screenshot(self.driver, '冒泡信息')
                return True
            else:
                return False

        if op == 'delete':
            # 冒泡信息获取
            if self.wait_element_until_visible(CategoryPage.__deletemessage):
                Untils.save_screenshot(self.driver, '冒泡信息')
                return True
            else:
                return False
