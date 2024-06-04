from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearch:

    def test_search(self):
        # 初始化浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("https://xueqiu.com/")
        self.driver.implicitly_wait(3)

        # 输入搜索关键词
        self.driver.find_element(By.NAME, "q").send_keys("阿里巴巴-SW")
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, "i.iconfont_iconfont_9UW.index_iconfont_mYK").click()
        # 获取搜索结果
        name = self.driver.find_element(By.XPATH, "//table//strong").text
        # 断言
        assert name == "阿里巴巴-SW"
