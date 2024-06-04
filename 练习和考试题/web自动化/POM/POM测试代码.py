import sys

sys.path.append("..\\POM")

from POM脚本 import SearchPage


class TestSearch:

    def setup(self):
        # 初始化搜索页面的建模类，创建操作对象
        self.tester = SearchPage()

    def teardown(self):
        # 操作对象调用quit方法关闭浏览器
        self.tester.quit()

    def test_search(self):
        # 调用serch_stock方法并传参搜索内容。结果返回给变量text
        text = self.tester.search_stock("阿里巴巴-SW")

        # 断言
        assert "阿里巴巴-SW" == text
