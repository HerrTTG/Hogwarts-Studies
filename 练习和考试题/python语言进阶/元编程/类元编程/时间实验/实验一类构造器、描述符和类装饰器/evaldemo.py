#!/usr/bin/env python3

from 练习和考试题.python语言进阶.元编程.类元编程.时间实验.实验二元类.builderlib import Builder, deco, Descriptor

print('# evaldemo module start')


@deco  # <1>类装饰器
class Klass(Builder):  # <2>子类继承导入的基类
    print('# Klass body')
    attr = Descriptor()  # <3>类属性绑定描述符实例

    def __init__(self):
        super().__init__()
        print(f'# Klass.__init__({self!r})')

    def __repr__(self):
        return '<Klass instance>'


def main():  # <4>
    obj = Klass()
    obj.method_a()
    obj.method_b()
    obj.attr = 999


if __name__ == '__main__':
    print("# run main")
    main()

print('# evaldemo module end')
