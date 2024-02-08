"""作业内容
完整的测试流程，包含需求分析、测试计划设计、测试用例编写、测试执行、bug 的提交与管理。
使用思维导图完成需求分分析；提供完整测试计划模板，完成测试计划设计；应用多种测试用例设计方法，包括：等价类、边界值、错误推测法等。
测试执行过程中应用多种测试方法完成计算器的加法、除法运算。
结合项目管理工具完成 bug 的提交与管理，进行测试报告编写与项目总结。
新增：
编写自动化测试用例，结合 Allure 细化测试报告，比如添加用例标题与用例步骤。
使用参数化减少代码量，提高代码的可维护性。
使用 mark 标签为测试用例分类
设置跳过、预期失败用例
对异常用例进行处理
"""
import allure
import pytest
import yaml

"""
需求分析:两个功能计算功能。分别是加法和除法。输入范围在【-99, 99】的整数或浮点数，超出范围将提示超出范围，否则返回计算结果。
"""

"""
测试计划设计:https://github.com/HerrTTG/Hogwarts-Studies/blob/main/homework/pytest%20and%20allure/%E6%B5%8B%E8%AF%95%E8%AE%A1%E5%88%92.docx
"""

"""
测试方法设计:
等价划分法
    -有效输入 0 34 5.5 0.1 -30 -60.4 
    -无效输入 1000 -232 中文 ~！@#￥ hello 空
边界值法
    - -100 -99  -98   98 99 100 
    - -99.1 99.0 -98.99  98.99 99.00 99.1 
"""

"""
测试结果:
利用Allure技术生成结果报告。
https://github.com/HerrTTG/Hogwarts-Studies/tree/main/homework/pytest_and_allure/%E8%AE%A1%E6%95%B0%E5%99%A8%E5%AE%9E%E6%88%98L1/my_html_report/html_dir
"""


# 被测代码
class Calculator:
    def add(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a + b

    def div(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a / b


@allure.epic('计算器需求')
class Test():
    @staticmethod
    def getdate(filename):
        if filename == '加法.yaml':
            with open('加法.yaml', "r", encoding='utf-8') as file:
                data1 = yaml.safe_load(file)
            return data1
        elif filename == '加法e.yaml':
            with open("加法e.yaml", "r", encoding='utf-8') as file:
                data3 = yaml.safe_load(file)
            return data3
        elif filename == "除法.yaml":
            with open("除法.yaml", "r", encoding='utf-8') as file:
                data2 = yaml.safe_load(file)
            return data2
        elif filename == "除法e.yaml":
            with open("除法e.yaml", "r", encoding='utf-8') as file:
                data4 = yaml.safe_load(file)
            return data4

    @allure.feature('加法功能')
    @allure.title("加法测试用例：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('加法.yaml'))
    def test_add(self, a, b, c):
        tester = Calculator()
        try:
            with allure.step('测试步骤一,计算结果'):
                sum = tester.add(a, b)
            with allure.step('测试步骤二,比较结果是否符合预期'):
                assert sum == c, '测试结果与预期不符'
        except:
            raise '其他错误'

    # 除法用例
    @allure.feature('除法功能')
    @allure.title("除法测试用例：{a}/{b}")
    @pytest.mark.parametrize("a, b, c", getdate('除法.yaml'))
    def test_div(self, a, b, c):
        tester = Calculator()
        try:
            with allure.step('测试步骤一,计算结果'):
                sum = tester.div(a, b)
            with allure.step('测试步骤二,比较结果是否符合预期'):
                assert sum == c, '测试结果与预期不符'
        except:
            raise '其他错误'

    # 加法异常场景

    @allure.story('加法功能异常场景')
    @allure.feature('加法功能')
    @pytest.mark.xfail
    @allure.title("加法异常用例：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('加法e.yaml'))
    def test_add_error(self, a, b, c):
        tester = Calculator()
        with allure.step('测试步骤一,尝试进行计算'):
            sum = tester.add(a, b)
        with allure.step('测试步骤二,用例应该失败，无法进行断言比较'):
            assert sum == c

    # 除法异常场景

    @allure.story('除法功能异常场景')
    @allure.feature('除法功能')
    @pytest.mark.xfail
    @pytest.mark.parametrize("a, b, c", getdate('除法e.yaml'))
    def test_div_error(self, a, b, c):
        tester = Calculator()
        # 动态更新用例标题，可以参与到用例执行中去增加当前用例的标题名
        allure.dynamic.title(f"除法异常用例:{a}/{b}")
        with allure.step('测试步骤一,尝试进行计算'):
            sum = tester.div(a, b)
        with allure.step('测试步骤二,用例应该失败，无法进行断言比较'):
            assert sum == c


# 加法用例
if __name__ == '__main__':
    pytest.main(['./计算器实战L2.py', '-vs'])
