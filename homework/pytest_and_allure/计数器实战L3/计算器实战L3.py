"""作业内容
完整的测试流程，包含需求分析、测试计划设计、测试用例编写、测试执行、bug 的提交与管理。
使用思维导图完成需求分分析；提供完整测试计划模板，完成测试计划设计；应用多种测试用例设计方法，包括：等价类、边界值、错误推测法等。
测试执行过程中应用多种测试方法完成计算器的加法、除法运算。
结合项目管理工具完成 bug 的提交与管理，进行测试报告编写与项目总结。
编写自动化测试用例，结合 Allure 与截图技术等自动生成带截图与操作步骤的测试报告。
使用参数化减少代码量，提高代码的可维护性。
使用 mark 标签为测试用例分类
设置跳过、预期失败用例
对异常用例进行处理

新增内容：
pytest fixture 实现测试装置及参数化
pytest conftest.py 的用法
pytest 文件配置 pytest.ini
考察：
掌握 Pytest 常用的装饰器，例如：添加标签、参数化、Fixture 等。
掌握 Pytest 自动化测试框架多种复杂配置，比如 pytest.ini 配置、conftest.py 配置等。



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
https://github.com/HerrTTG/Hogwarts-Studies/tree/main/homework/pytest_and_allure/%E8%AE%A1%E6%95%B0%E5%99%A8%E5%AE%9E%E6%88%98L2/report/html_dir
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


##用例设计##

@allure.epic('计算器需求')
class Test():
    @staticmethod
    def getdate(filename) -> list:
        """
        静态方法，被class下其他用例调用。
        输入：文件名
        输出：根据文件名来获取yaml文件中的参数数据，并返回一个list
        """
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
        else:
            raise '初始化参数文件失败，输入的文件名不正确'

    @pytest.mark.basetest
    @allure.feature('加法功能')
    @allure.story('加法一般场景')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("加法测试用例：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('加法.yaml'))
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

    # 除法用例
    @pytest.mark.basetest
    @allure.feature('除法功能')
    @allure.story('除法一般场景')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("除法测试用例：{a}/{b}")
    @pytest.mark.parametrize("a, b, c", getdate('除法.yaml'))
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

    # 加法无效场景
    @pytest.mark.advtest
    @allure.feature('加法功能')
    @allure.story('加法无效场景')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.xfail
    @allure.title("加法无效场景：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('加法e.yaml'))
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

    # 除法无效场景
    @pytest.mark.xfail
    @pytest.mark.advtest
    @allure.feature('除法功能')
    @allure.story('除法无效场景')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("a, b, c", getdate('除法e.yaml'))
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

    # 异常抛出测试
    # 加法异常抛出测试
    @pytest.mark.advtest
    @allure.feature('加法功能')
    @allure.story('加法异常场景')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title("加法异常场景{c}：{a}+{b}")
    @pytest.mark.parametrize("a, b, c", getdate('加法e.yaml'))
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

    # 除法异常抛出测试
    @pytest.mark.advtest
    @allure.feature('除法功能')
    @allure.story('除法异常场景')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title("除法异常场景:")
    @pytest.mark.parametrize("a, b, c", getdate('除法e.yaml'))
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


# 加法用例
if __name__ == '__main__':
    pytest.main(['./计算器实战L3.py', '-vs'])
