"""
__author__ = 'hogwarts_xixi'
"""
import pytest


def test_raise():
    # with pytest.raises(异常)表示with下面的代码在运行的时候，如果遇到抛出对应的异常，将不会退出 会继续执行。
    # match是msg的正则匹配
    with pytest.raises((ZeroDivisionError, ValueError), match='除数为0'):
        raise ZeroDivisionError("除数为0")
        raise ValueError('我到这里了')


def test_raise1():
    # 也可以将其重命名为一个对象
    # 来获取异常的type属性以及value属性中对应的msg信息
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"
