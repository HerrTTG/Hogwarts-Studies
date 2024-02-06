import pytest


# pip install allure-pytest and allure

def test_case1():
    assert True


def test_case2():
    assert False


@pytest.mark.skip
def test_case3():
    assert 1 + 1 == 2
