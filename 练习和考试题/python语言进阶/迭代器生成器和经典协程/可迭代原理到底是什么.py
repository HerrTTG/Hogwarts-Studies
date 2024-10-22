import re


class Seq():
    re_word = re.compile(r'\w+')

    def __init__(self, words):
        self.words = self.re_word.findall(words)  # 根据正则表达式，匹配出所有符合要求的单词，并返回列表。

    def __getitem__(self, item):
        # 实现自我迭代
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return f'Seq{self.words}'


# 测试Seq的实例化对象是否可迭代
words = Seq("The time has come ,the Jon said. ")
for i in words:
    print(i)
