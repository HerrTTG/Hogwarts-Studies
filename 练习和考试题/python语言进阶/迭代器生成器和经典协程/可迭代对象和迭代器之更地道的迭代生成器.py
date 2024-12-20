import re


class Seq():
    re_word = re.compile(r'\w+')

    def __init__(self, words):
        self.words = self.re_word.findall(words)  # 根据正则表达式，匹配出所有符合要求的单词，并返回列表。

    # def __getitem__(self, item):
    #     return self.words[item]

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return f'Seq{self.words}'

    def __iter__(self):
        # 此时此函数是一个生成器，
        for words in self.words:  # 迭代self.words这个标准库序列
            yield words  # 生成器函数表达时。
            # 不再用单独定义迭代器了！
            # 迭代的实现不在需要委托迭代Iterator构造实例化对象了。


# 测试Seq的实例化对象是否可迭代
words = Seq("The time has come ,the Jon said. ")
for i in words:
    print(i)
