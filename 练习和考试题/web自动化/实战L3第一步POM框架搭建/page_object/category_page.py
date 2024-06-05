from page_object.BasePage import BasePage


class CategoryPage(BasePage):
    def click_add(self):
        # 商品列表管理页面：点击添加
        # 点击添加

        # =>>跳转添加商品表单
        from page_object.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    def click_search(self):
        # 商品列表管理页面：点击查询
        # 输入框输入搜索内容
        # 点击查询
        # 返回符合结果的数据的元素
        ele = self.do_find()
        return ele

    def click_delete(self, ele):
        # 商品列表管理页面：删除商品
        # 获取符合结果的数据的元素ele所在的位置的delete元素位置
        # 点击delete按钮
        pass

    def get_opertor_result(self):
        # 冒泡信息获取

        # 返回冒泡信息
        return "message"
