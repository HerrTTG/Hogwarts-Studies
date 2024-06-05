import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 目标1： 实现代码异常的时候，截图/打印page_source
# 简单实现方法： try catch 配合截图/ page_source操作
# ===问题1： 异常处理会影响用例本身的结果
# 解决方案： 在exception 之后再把异常抛出

# ===问题2： 异常捕获处理代码和业务代码无关，不能耦合
# 解决方案： 使用装饰器装饰用例或者相关方法，就不会体现在源码中了（注意：！！！一定要先学习装饰器）


def ui_exception_record(func):
    # 装饰器的解决思路
    # 1. 先把装饰器的架子搭好
    # 2. 把相关逻辑嵌套进来
    def inner(*args, **kwargs):
        try:
            # =====问题4： 隐藏的小bug，一旦被装饰方法有返回值，会丢失返回值
            # 解决方案：  # 当被装饰方法/函数发生异常就捕获并做数据记录
            # 如果被装饰函数需要返回值，装饰器内调用就不能缺少return关键字
            return func(*args, **kwargs)
        except Exception:
            # 获取被装饰方法的self 也就是实例对象
            # 通过self 就可以拿到声明的实例变量driver
            # 前提条件： 1. 被装饰的方法是一个实例方法， 2. 实例需要有实例变量self.driver
            # 问题： 被装饰函数还没有执行，所以还没有self.driver
            # 解决方案1： 获取driver 放在函数执行之后
            # 解决方案2： 保证使用装饰器的时候，driver 已经声明（setup）
            # 方案1# 获取driver 此时被装饰的函数已经运行，所以对象拥有了driver
            driver = args[0].driver

            # 截图操作
            timestamp = int(time.time())
            # 注意：！！ 一定要提前创建好images 路径
            image_path = f"./report/images/image_{timestamp}.PNG"
            page_source_path = f"./report/page_sources/page_source_{timestamp}.html"
            # 截图
            driver.save_screenshot(image_path)
            ## 记录page_source
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(driver.page_source)
            # 讲截图放到报告的数据中
            allure.attach.file(image_path, name="picture",
                               attachment_type=allure.attachment_type.PNG)
            # 将pagesource 记录到报告中
            # 如果想要 html 源码格式使用text 如果想要页面格式就用html
            # allure.attach.file(page_source_path, name="pagesource",
            #                    attachment_type=allure.attachment_type.HTML)
            allure.attach.file(page_source_path, name="pagesource",
                               attachment_type=allure.attachment_type.TEXT)
            raise Exception

    return inner


class TestBaidu:

    def setup_class(self):
        # 方案2 直接声明driver 后续装饰器也将拥有self.driver
        self.driver = webdriver.Chrome()

    @ui_exception_record
    def find(self):
        return self.driver.find_element(By.ID, "su1")

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.find().click()
        self.driver.quit()
