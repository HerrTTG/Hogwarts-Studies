from page_object.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        from page_object.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    def click_search(self, seach_name):
        # 商品列表管理页面：点击查询
        # 输入框输入搜索内容
        self.do_send(seach_name, CategoryPage.__serchbyname)
        # 点击查询
        self.do_click(CategoryPage.__serchbutton)
        # 搜索所有结果列
        eles = self.do_finds(CategoryPage.__serchrow)
        for i in eles:
            # 对每一行校验第三列name是否为输入的查询关键字 返回row
            if i.find_element(*CategoryPage.__rowname). \
                    get_attribute('innerText') == seach_name:
                return i
        else:
            return False

    def click_delete(self, row):
        # 商品列表管理页面：删除商品
        # 获取符合结果的数据的元素ele所在的位置的delete元素位置
        # 对row查询row内的删除按钮
        # 点击delete按钮
        row.find_element(*CategoryPage.__deletebutton).click()

    def get_opertor_result(self, op):
        if op == 'add':
            # 冒泡信息获取
            if WebDriverWait(self.driver, 5, 1).until(
                    expected_conditions.visibility_of_element_located(CategoryPage.__addmessage)):
                # 返回冒泡信息
                return "创建成功"

        if op == 'delete':
            # 冒泡信息获取
            if WebDriverWait(self.driver, 5, 1).until(
                    expected_conditions.visibility_of_element_located(CategoryPage.__deletemessage)):
                # 返回冒泡信息
                return "删除成功"
