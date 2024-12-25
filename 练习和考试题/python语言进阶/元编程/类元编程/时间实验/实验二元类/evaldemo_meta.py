#!/usr/bin/env python3

from builderlib import Builder, deco, Descriptor
from metalib import MetaKlass  # <1>导入元类

print('# evaldemo_meta module start')


@deco
class Klass(Builder, metaclass=MetaKlass):  # <2>指定元类为我们导入的元类
    print('# Klass body')

    attr = Descriptor()

    def __init__(self):
        super().__init__()
        print(f'# Klass.__init__({self!r})')

    def __repr__(self):
        return '<Klass instance>'


def main():
    obj = Klass()
    obj.method_a()
    obj.method_b()
    obj.method_c()  # <3>新加入的由元类注入的方法
    obj.attr = 999


if __name__ == '__main__':
    print("# run main")
    main()

print('# evaldemo_meta module end')
