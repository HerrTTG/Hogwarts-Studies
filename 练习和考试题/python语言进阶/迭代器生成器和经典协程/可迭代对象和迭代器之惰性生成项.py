import re


class Seq():
    re_word = re.compile(r'\w+')

    def __init__(self, words):
        self.words = words  # 不在构造列表，而是直接别名。惰性处理数据

    # def __getitem__(self, item):
    #     return self.words[item]
    # 不自我实现迭代，而是交给迭代器实现迭代

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return f'Seq{self.words}'

    def __iter__(self):
        # 此时此函数其实已经是生成器了
        # 惰性是指尽可能延后生成值
        # 在这个案例中，可迭代对象Seq并不构造列表。
        # 迭代的实现也由迭代器转为生成器。

        # 有点还没看明白
        for match in self.re_word.finditer(self.words):  # finditer函数将构造一个生成器，包含words中匹配的单词。
            # 仅在需要时，才从文本中读取下一个符合正则表达式的内容。
            yield match.group()


# 测试Seq的实例化对象是否可迭代
words = Seq("The time has come ,the Jon said. ")
for i in words:
    print(i)
