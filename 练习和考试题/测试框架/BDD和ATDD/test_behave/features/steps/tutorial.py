from behave import *
from selenium import webdriver


@given('we have behave installed')
def step_impl(context):
    print("given run")
    pass


@when('we implement a test')
def step_impl(context):
    print('when run')
    assert True is not False
    # assert 1 == 2


@when('打开浏览器访问 ceshiren.com')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('https://ceshiren.com')
    print("打开完成")


@then('behave will test it for us!')
def step_impl(context):
    print('then run')
    assert context.failed is False
