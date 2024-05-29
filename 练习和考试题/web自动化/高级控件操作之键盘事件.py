import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeyBoardDemo:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_key_down_up(self):
        """
        ActionChains(self.driver): 实例化ActionChains类
        key_down(Keys.SHIFT, ele): 按下shift键实现大写
        send_keys("selenium"): 输入大写的selenium
        perform(): 确认执行
        """
        # 演练环境
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # 定义目标元素，即输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # 用链式高级控件，传入driver初始化
        # 调用key_down方法 按下Keys.SHIFT shift键
        # 同时输入selenium 到目标元素
        ActionChains(self.driver).key_down(Keys.SHIFT, ele). \
            send_keys("selenium").perform()
        time.sleep(3)

    def test_enter(self):
        """
        直接输入回车: 元素.send_keys(Keys.ENTER)
        使用ActionChains: key_down(Keys.ENTER)
        """
        # 演练环境
        self.driver.get("https://www.sogou.com/")

        # 定位目标元素，即搜狗的搜索输入框
        ele = self.driver.find_element(By.ID, "query")

        # #第一种方式
        # #元素输入内容
        # #元素按回车
        # ele.send_keys("selenium")
        # ele.send_keys(Keys.ENTER)

        # 第二种方式
        # #用链式高级控件
        # #输入内容到元素
        # #之后跟按回车
        ActionChains(self.driver). \
            send_keys_to_element(ele, "selenium"). \
            key_down(Keys.ENTER). \
            perform()
        time.sleep(3)

    def test_copy_and_paste(self):
        """
        多系统兼容
        mac 的复制按钮为 COMMAND
        windows 的复制按钮为 CONTROL
        左箭头：Keys.ARROW_LEFT
        按下COMMAND或者CONTROL: key_down(cmd_ctrl)
        按下剪切与粘贴按钮: send_keys("xvvvvv")
        """
        # 演练环境
        self.driver.get("https://ceshiren.com/")

        # 判断操作系统，darwin 即为mac 复制按钮为 COMMAND
        # 否则为Keys.CONTROL
        cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

        # 点击搜索按钮
        self.driver.find_element(By.ID, "search-button").click()

        # 定位输入框元素
        ele = self.driver.find_element(By.ID, "search-term")

        # 按下shift键输入selenium，在不放开shift键的情况下输入左键 效果为shift+← 选择内容，连续按几次左就表示选择几位
        # 然后松开shift，按下CTRL键，之后输入X 和C 表示剪切和粘贴
        # 最后放开CTRL键
        ActionChains(self.driver) \
            .key_down(Keys.SHIFT) \
            .send_keys_to_element(ele, "Selenium!") \
            .send_keys(Keys.ARROW_LEFT) \
            .key_up(Keys.SHIFT) \
            .key_down(cmd_ctrl) \
            .send_keys("xvvvvv") \
            .key_up(cmd_ctrl) \
            .perform()
        time.sleep(5)
