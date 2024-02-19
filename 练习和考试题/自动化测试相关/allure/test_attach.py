import allure


class TestWithAttach:
    # 方法一 直接添加一个文件作为附件
    def test_pic(self):
        allure.attach.file("./微信截图_20240219142704.png",
                           name="图片",
                           attachment_type=allure.attachment_type.PNG,
                           extension="png")

    # 方法二 添加一个可读取的数据作为对象
    def test_pic2(self):
        with open("./微信截图_20240219142704.png", 'rb') as f:
            file = f.read()
            allure.attach(file, name='图片2', attachment_type=allure.attachment_type.PNG,
                          extension="png")
