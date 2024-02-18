import pytest


@pytest.fixture()
def loing():
    print("loging...")


def test_serch():
    print("搜索")


# 传入被装饰的login函数名，就代表此用例在运行前需要先运行login
def test_cart(loing):
    print("购物")
