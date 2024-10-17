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
        # 此时此函数其实已经是生成器了
        for match in self.re_word.finditer(self.words):  # finditer将构造一个迭代器，包含words中匹配的单词。
            # 仅在需要时，才从文本中读取下一个符合正则表达式的内容
            yield match.group()


# 测试Seq的实例化对象是否可迭代
words = Seq("The time has come ,the Jon said. ")
for i in words:
    print(i)
