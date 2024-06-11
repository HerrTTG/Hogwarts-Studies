import allure
import os
import time
import yaml
from datetime import  datetime



class Untils():
    @classmethod
    def get_path(cls):
        """
        获取path方法
        """
        ## ..\\..\\L2
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(path)
        return path

    @classmethod
    def envfileload(cls, env):
        """
        根据命令行获取，从不同的配置文件中获取环境信息
        """
        myenv = env
        if myenv == 'test':
            print('获取并返回环境信息，此条为测试环境')
            with open(f'{Untils.get_path()}\\config\\envtest.yaml', 'r') as file:
                envinfo = yaml.safe_load(file)
        elif myenv == 'dev':
            print('获取并返回环境信息，此条为开发环境')
            with open(f'{Untils.get_path()}\\config\\devtest.yaml', 'r') as file:
                envinfo = yaml.safe_load(file)
        return envinfo

    @classmethod
    def get_testdata(cls):
        """
        获取测试数据方法，用例中输入的测试数据都由文件形式保存。不体现在用例中
        """
        with open(f'{Untils.get_path()}\\datas\\testdata.yaml', 'r', encoding='utf-8') as file:
            testdata = yaml.safe_load(file)
        # ['SeleniumA', 'Appium面', '面试']
        return testdata

    @classmethod
    def save_screenshot(cls, driver, id=0, message='NA'):
        if os.path.exists(f'{Untils.get_path()}\\datas\\images\\') is False:
            os.mkdir(f'{Untils.get_path()}\\datas\\images\\')

        file = f'{Untils.get_path()}\\datas\\images\\screenshot_{message}_{id}_{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.png'
        driver.save_screenshot(file)
        allure.attach.file(file, name=message,
                           attachment_type=allure.attachment_type.PNG)

    @classmethod
    def save_page_soure(cls, driver, id=0, message='NA'):
        if os.path.exists(f'{Untils.get_path()}\\datas\\pagesouces\\') is False:
            os.mkdir(f'{Untils.get_path()}\\datas\\pagesouces\\')

        file = f'{Untils.get_path()}\\datas\\pagesouces\\{message}_{id}_{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.html'
        with open(file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        allure.attach.file(file, name=message, attachment_type=allure.attachment_type.TEXT)
