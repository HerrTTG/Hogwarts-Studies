"""
__author__ = 'hogwarts_xixi'
"""
import pytest
import sys


@pytest.mark.skip
def test_aaa():
    print("代码未开发完")
    assert True


@pytest.mark.skip(reason="存在bug")
def test_bbb():
    assert False


# if not sys.platform.startswith("darwin"):
#     pytest.skip("skipping windows-only tests", allow_module_level=True)

## 代码中添加 跳过代码块 pytest.skip(reason="")
def check_login():
    return False


def test_function():
    print("start")
    print(sys.platform)
    # 如果未登录，则跳过后续步骤
    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")


@pytest.mark.skipif(sys.platform == 'darwin', reason="does not run on mac")
def test_case1():
    assert True


@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
def test_case2():
    assert True


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_case3():
    assert True


def test_xfail():
    print("*****开始测试*****")
    pytest.xfail(reason='该功能尚未完成')
    print("测试过程")
    assert 1 == 1


@pytest.mark.xfail
def test_ccc():
    print("test_xfail1 方法执行，可用于标记尚未解决的bug。通过可能是规避操作")
    assert 1 == 1


xfail = pytest.mark.xfail


@xfail(reason="bug 110")
def test_hello4():
    print("test_xfail1 方法执行，可用于标记尚未解决的bug。失败可能是bug未解决")
    assert 0
