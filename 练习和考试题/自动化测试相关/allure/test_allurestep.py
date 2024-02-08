"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
# 方法一：使用装饰器定义一个测试步骤，在测试用例中使用
import allure
import pytest


# 方法一：使用装饰器添加测试步骤
# 定义测试步骤：simple_step1
@allure.step
def _step1(step_param1, step_param2=None):
    '''定义一个测试步骤'''
    print("首先：连接数据库，准备测试数据")
    print(f"步骤1：打开页面1，参数1: {step_param1}, 参数2：{step_param2}")


# # 定义测试步骤：simple_step2
@allure.step
def _step2(step_param):
    '''定义一个测试步骤'''
    assert False
    print(f"步骤2：完成搜索 {step_param} 功能")


@allure.title("Test case 1")
@pytest.mark.parametrize('param1', ["pytest", "allure"], ids=['search pytest', 'search allure'])
def test_parameterize_with_id(param1):
    _step2(param1)


@allure.title("Test case 2")
@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    _step1(param1, param2)


@allure.title("Tese case 3")
@pytest.mark.parametrize('param2', ['pytest', 'unittest'])
@pytest.mark.parametrize('param1,param3', [[1, 2]])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    _step1(param1, param3)
    _step2(param2)


# 方法二：使用 `with allure.step()` 添加测试步骤
@allure.title("搜索用例:{searchkey}")
@pytest.mark.parametrize("searchkey", ["pytest", "allure"])
def test_step_in_method(searchkey):
    with allure.step("测试步骤一：打开页面"):
        print("操作 a")
        print("操作 b")

    with allure.step(f"测试步骤二：搜索{searchkey}"):
        print(f"搜索操作 : {searchkey}")

    with allure.step("测试步骤三：断言"):
        assert False
