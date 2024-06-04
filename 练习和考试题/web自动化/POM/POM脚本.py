from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage:
    """
    对搜索页面进行建模
    """

    # 第一步，元素定位变为内部类属性
    __INPUT_SEARCH = (By.NAME, "q")
    __BUTTON_SEARCH = (By.CSS_SELECTOR, "i.iconfont_iconfont_9UW.index_iconfont_mYK")
    __SPAN_STOCK = (By.XPATH, "//table//strong")

    # 第二步，定义初始化信息
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://xueqiu.com/")

    # 第三步，封装页面操作动作和对应元素为方法
    def search_stock(self, stock_name: str):
        # 搜索方法
        self.driver.find_element(*SearchPage.__INPUT_SEARCH).send_keys(stock_name)
        self.driver.find_element(*SearchPage.__BUTTON_SEARCH).click()
        name = self.driver.find_element(*SearchPage.__SPAN_STOCK).text

        return name

    def quit(self):
        self.driver.quit()
