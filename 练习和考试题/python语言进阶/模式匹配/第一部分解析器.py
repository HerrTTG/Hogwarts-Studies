# 将scheme的表达式解析为python代码运算的第一部分


# 导入和定义类型
from typing import TypeAlias

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list


# 解析器主体
def parse(program: str) -> Expression:
    # 从字符串中读取Scheme表达式
    return read_from_token(tokenize(program))


def read_from_token(token: list[str]) -> Expression:
    # 从列表中的元素中提取出表达式单词
    return token


def tokenize(s: str) -> list[str]:
    # 解决Scheme表达式中的括号。塞空格符，方便拆分为列表元素。
    return s.replace('(', ' ( ').replace(')', ' ) ').split()


if __name__ == '__main__':
    print(parse('(gcd 18 45)'))
    # 返回为['(', 'gcd', '18', '45', ')']
