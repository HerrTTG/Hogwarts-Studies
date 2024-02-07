import pytest


# 被测代码
def add_one(x):
    return x + 1


# 函数级的测试用例
@pytest.mark.apptest
def test_func():
    result = add_one(10)
    assert result == 11


@pytest.mark.webtest
def test_func2():
    result = add_one(10)
    assert result == 11


@pytest.mark.iostest
def test_func3():
    result = add_one(10)
    assert result == 12, '结果不对'


# 可不写,直接执行这里，效果和点最上面的播放键一样
if __name__ == '__main__':
    pytest.main()
