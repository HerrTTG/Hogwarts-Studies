from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 根据frame 的id 切换对应的frame
        self.driver.switch_to.frame("iframeResult")

        # 切换frame后 直接对frame内的html进行元素搜索
        print(self.driver.find_element(By.ID, "draggable").text)

        # 切换父frame 即上层frame
        # self.driver.switch_to.parent_frame()

        # 切换默认frame 即最外层dom的frame
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, "submitBTN").text)
