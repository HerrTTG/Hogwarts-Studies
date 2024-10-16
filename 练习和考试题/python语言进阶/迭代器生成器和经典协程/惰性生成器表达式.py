import re


class Seq():
    re_word = re.compile(r'\w+')

    def __init__(self, words):
        self.words = words  # 不在构造列表，而是直接别名。惰性处理数据

    # def __getitem__(self, item):
    #     return self.words[item]

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return f'Seq{self.words}'

    def __iter__(self):
        # 直接返回一个生成器表达式也就是生成器对象
        return (match.group() for match in self.re_word.finditer(self.words))


# 测试Seq的实例化对象是否可迭代
words = Seq("The time has come ,the Jon said. ")
for i in words:
    print(i)
