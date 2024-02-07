import pytest


def func(a, b):
    print(a, b)


# 笛卡尔积参数化写法。a1 a2 a3 b1 b2 b3  .....
@pytest.mark.parametrize("b", [1, 2, 3])
@pytest.mark.parametrize("a", ['a', 'b', 'c'])
def test_case(a, b):
    func(a, b)
