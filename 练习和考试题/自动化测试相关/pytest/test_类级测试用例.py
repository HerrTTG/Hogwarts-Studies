import pytest


# 被测代码
def add_one(x):
    return x + 1


class Testclass():
    # 类级测试用例不能写构造函数
    def test_answer(self):
        assert add_one(1) == 2

    def test_answer1(self):
        assert add_one(2) == 3

    def test_answer2(self):
        assert add_one(10) == 12


# 可不写,效果和点最上面的播放键一样
if __name__ == '__main__':
    pytest.main()
