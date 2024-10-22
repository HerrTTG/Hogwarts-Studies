import re

class SeqIterator:
    # 迭代器
    def __init__(self, words):
        # 构造传入的数据，并初始化索引为后面next方法返回迭代值做准备
        self.words = words
        self.index = 0

    def __iter__(self):
        return self  #返回迭代器对象，以方便调用next使用迭代器


    def __next__(self):
        #当next函数执行时，调用__next__
        try:
            # 根据索引获取序列中的值
            words = self.words[self.index]
        except IndexError:
            #获取失败则抛出迭代结束异常
            raise StopIteration()
        else:
            # 成功获取，则索引+1.且无法回头和重置。
            # 返回获取值
            self.index+=1
            return words


class Seq():
    # 可迭代对象

    #定义类变量，一个正则表达式。
    re_word = re.compile(r'\w+')

    def __init__(self, words):
        self.words = self.re_word.findall(words)  #根据正则表达式，匹配出所有符合要求的单词，并返回列表。

    # def __getitem__(self, item):
    #     return self.words[item]
    #不自我实现迭代，而是交给迭代器实现迭代

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return f'Seq{self.words}'

    def __iter__(self):
        # 可迭代对象被要求迭代时，即iter(self),执行self.__iter__方法
        # 返回由迭代器构造的实例对象。
        return SeqIterator(self.words)
        # 由于迭代器的不可重置特性，所以需要重新迭代可迭代对象时，要重新执行iter(x)
        #即重新执行对象的该方法，该方法会生成新的迭代器对象


# 测试Seq的实例化对象是否可迭代
words = Seq("The time has come ,the Jon said. ")
for i in words:
    print(i)