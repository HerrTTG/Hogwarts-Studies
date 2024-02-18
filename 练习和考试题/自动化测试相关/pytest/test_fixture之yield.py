import pytest


# 默认是function级别的
@pytest.fixture(scope="module")
def loing():
    print("登录完成")
    token = '12341231'
    userid = 'kuoka'
    # yield 相当于return 可以同时带数据返回
    yield token, userid
    print('登录结束')


def test_serch(loing):
    print(f"搜索{loing}")


def test_cart(loing):
    print(f"购物{loing}")
