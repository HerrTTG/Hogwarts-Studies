import pytest


# 默认是function级别的
@pytest.fixture(scope="module")
def loing():
    print("登录完成")


def test_serch(loing):
    print("搜索")


def test_cart(loing):
    print("购物")
