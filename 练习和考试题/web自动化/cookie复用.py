import time
import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_method(self):
        self.drvier = webdriver.Chrome()

    def teardown_method(self):
        self.drvier.quit()

    def test_get_cookies(self):
        # 1. 访问企业微信主页/登录页面
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 2. 无限等待人工扫码操作，直到获取到的cookie为登录后的长度
        while True:
            cookie = self.drvier.get_cookies()
            if len(cookie) == 12:
                with open("cookie.yaml", "w") as f:
                    # 第一个参数是要写入的数据
                    # 3.将cookie存入一个可持久存储的地方，文件
                    yaml.safe_dump(cookie, f)
                break
            else:
                time.sleep(3)

    def test_add_cookie(self):
        # 1. 访问企业微信主页面
        # 测试直接访问仍需扫码
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(3)

        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("cookie.yaml"))

        # 3. 植入cookie 因为cookie读取出来为列表，需要循环一个一个加入
        # 另外需要格外注意
        # 加cookie必须先到要加的cookie域名下
        # 所以先访问域名再加
        for c in cookie:
            self.drvier.add_cookie(c)

        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(3)
