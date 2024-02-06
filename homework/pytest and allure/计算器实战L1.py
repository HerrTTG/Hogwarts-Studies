"""作业内容
1．完整的测试流程，包含需求分析、测试计划设计、测试用例编写、测试执行、bug 的提交与管理。
2．使用思维导图完成需求分分析；提供完整测试计划模板，完成测试计划设计；应用多种测试用例设计方法，包括：等价类、边界值、错误推测法等。
3．测试执行过程中应用多种测试方法完成计算器的加法、除法运算。
4．结合项目管理工具完成 bug 的提交与管理，进行测试报告编写与项目总结。
5．编写自动化测试用例，结合 Allure 技术生成测试报告。
"""
import pytest
import yaml

"""
需求分析:两个功能计算功能。分别是加法和除法。输入范围在【-99, 99】的整数或浮点数，超出范围将提示超出范围，否则返回计算结果。
"""

"""
测试计划设计:
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


with open("加法.yaml", "r", encoding='utf-8') as file:
    data1 = yaml.safe_load(file)


@pytest.mark.parametrize("a, b, c", data1)
def test_add1(a, b, c):
    tester = Calculator()
    try:
        assert tester.add(a, b) == c, '测试结果与预期不符'
    except TypeError:
        pass


if __name__ == '__main__':
    pytest.main()
