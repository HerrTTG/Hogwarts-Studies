'''
新增：
数据驱动
pytest fixture
pytest conftest.py 的用法
"""
'''
import allure
import pytest
import sys
import time
import yaml

sys.path.append('../func')

from 计算器 import Calculator


##用例设计##

@allure.epic('计算器需求')
class Test():
    @staticmethod
    def getdate(filename) -> list:
        """
        获取yaml数据方法。
        输入：文件名
        输出：根据文件名来获取yaml文件中的参数数据，并返回一个list
        """
        try:
            with open(filename, "r", encoding='utf-8') as file:
                data1 = yaml.safe_load(file)
            return data1
        except:
            raise 'error'

    @pytest.mark.basetest
    @allure.feature('加法功能')
    @allure.story('加法一般场景')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("加法测试用例：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('../datas/加法.yaml'))
    def test_add(self, a, b, c):
        """
        计算器基础功能的加法用例。
        使用数据参数化的方法,调用getdate函数获取用例的参数。
        步骤一：
        计算a+b
        步骤二：
        断言a+b==c
        超出范围的无效输入返回 参数大小超出范围
        参数大小超出范围 亦由参数化带入c变量中
        """
        tester = Calculator()
        try:
            with allure.step('测试步骤一,计算结果'):
                sum = tester.add(a, b)
            with allure.step('测试步骤二,比较结果是否符合预期'):
                assert sum == c, '测试结果与预期不符'
        except:
            raise '其他错误'
        time.sleep(1)

    # 除法用例
    @pytest.mark.basetest
    @allure.feature('除法功能')
    @allure.story('除法一般场景')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("除法测试用例：{a}/{b}")
    @pytest.mark.parametrize("a, b, c", getdate('../datas/除法.yaml'))
    def test_div(self, a, b, c):
        """
        计算器基础功能的除法用例。
        使用数据参数化的方法,调用getdate函数获取用例的参数。
        步骤一：
        计算a/b
        步骤二：
        断言a/b==c
        超出范围的无效输入返回 参数大小超出范围
        参数大小超出范围 亦由参数化带入c变量中
        """
        tester = Calculator()
        try:
            with allure.step('测试步骤一,计算结果'):
                sum = tester.div(a, b)
            with allure.step('测试步骤二,比较结果是否符合预期'):
                assert sum == c, '测试结果与预期不符'
        except:
            raise '其他错误'
        time.sleep(1)

    # 加法无效场景
    @pytest.mark.advtest
    @allure.feature('加法功能')
    @allure.story('加法无效场景')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.xfail
    @allure.title("加法无效场景：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('../datas/加法e.yaml'))
    def test_add_error(self, a, b, c):
        """
        计算器进阶功能的无效用例。
        使用数据参数化的方法,调用getdate函数获取用例的参数。
        步骤一：
        计算a+b
        步骤二：
        断言a+b==c
        因为输入中a或者b中包含一些无效的非整数输入，
        所以用例将会失败。用xfail进行标记。
        """
        tester = Calculator()
        with allure.step('测试步骤一,尝试进行计算'):
            sum = tester.add(a, b)
        with allure.step('测试步骤二,用例应该失败，无法进行断言比较'):
            assert sum == c
        time.sleep(1)

    # 除法无效场景
    @pytest.mark.xfail
    @pytest.mark.advtest
    @allure.feature('除法功能')
    @allure.story('除法无效场景')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("a, b, c", getdate('../datas/除法e.yaml'))
    def test_div_error(self, a, b, c):
        """
        计算器进阶功能的无效用例。
        使用数据参数化的方法,调用getdate函数获取用例的参数。
        步骤一：
        计算a/b
        步骤二：
        断言a/b==c
        因为输入中a或者b中包含一些无效的非整数输入，
        所以用例将会失败。用xfail进行标记。
        """
        tester = Calculator()
        # 动态更新用例标题，可以参与到用例执行中去增加当前用例的标题名
        allure.dynamic.title(f"除法无效用例:{a}/{b}")
        with allure.step('测试步骤一,尝试进行计算'):
            sum = tester.div(a, b)
        with allure.step('测试步骤二,用例应该失败，无法进行断言比较'):
            assert sum == c
        time.sleep(1)

    # 异常抛出测试
    # 加法异常抛出测试
    @pytest.mark.advtest
    @allure.feature('加法功能')
    @allure.story('加法异常场景')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title("加法异常场景{c}：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('../datas/加法e.yaml'))
    def test_add_raise(self, a, b, c):
        """
        计算器进阶功能的异常处理用例。
        使用数据参数化的方法,调用getdate函数获取用例的参数。
        步骤一：
        计算a+b
        步骤二：
        断言errinfo.type is TypeError
        因为输入中a或者b中包含一些无效的非整数输入，应该抛出TypeError。
        用异常捕获的方法来判断的异常是否符合预期，对于其他异常将抛出失败。
        c变量用参数化来传入异常类型。
        """
        tester = Calculator()
        try:
            with allure.step('测试步骤一,尝试进行计算'):
                with pytest.raises(TypeError) as errinfo:
                    tester.add(a, b)
                    with allure.step('测试步骤二,判断抛出的异常是否为预知的异常报错'):
                        assert errinfo.type is c, '其他不符合预期的异常类型'
        except:
            assert False, '用例执行过程中失败'
        time.sleep(1)

    # 除法异常抛出测试
    @pytest.mark.advtest
    @allure.feature('除法功能')
    @allure.story('除法异常场景')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title("除法异常场景:")
    @pytest.mark.parametrize("a, b, c", getdate('../datas/除法e.yaml'))
    def test_div_raise(self, a, b, c):
        """
        计算器进阶功能的异常处理用例。
        使用数据参数化的方法,调用getdate函数获取用例的参数。
        步骤一：
        计算a/b
        步骤二：
        断言errinfo.type is TypeError 或者errinfo.type is ZeroDivisionError。
        因为输入中a或者b中包含一些无效的非整数输入，应该抛出TypeError。
        且被除数为0时抛出的异常应该为ZeroDivisionError。
        用异常捕获的方法来判断的异常是否符合预期，对于其他异常将抛出失败。
        c变量用参数化来传入异常类型。
        """
        tester = Calculator()
        # 动态更新用例标题，可以参与到用例执行中去增加当前用例的标题名
        allure.dynamic.title(f"除法异常用例{c}:{a}/{b}")
        try:
            with allure.step('测试步骤一,尝试进行计算'):
                # 多个异常种类需要用tuple来传递
                with pytest.raises((TypeError, ZeroDivisionError)) as errinfo:
                    tester.div(a, b)
                    with allure.step('测试步骤二,判断抛出的异常是否为预知的异常报错'):
                        assert errinfo is c, '其他不符合预期的异常类型'

        except:
            assert False, '用例执行过程中失败'
        time.sleep(1)


# 加法用例
if __name__ == '__main__':
    pytest.main(['./计算器实战L3.py', '-vs'])
