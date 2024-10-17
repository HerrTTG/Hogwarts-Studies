def chain(*iterable):
    for it in iterable:
        for i in it:
            yield i


a = '123'
b = range(3)

for i in chain(a, b):
    print(i)


def chain_new(*iterable):
    for it in iterable:
        yield from it


for i in chain_new(a, b):
    print(i)


# 以遍历类和子类为例
def tree(cls, level=0):
    # 树状遍历生成器
    # 先提供clsname和所属级别
    yield cls.__name__, level
    # 下一次迭代开始遍历下属子类
    for sub_cls in cls.__subclasses__():
        # 利用yield from 委托tree函数生成一个对下属子类进行迭代的子生成器，开始迭代。
        yield from tree(sub_cls, level + 1)
        # 直到子生成器迭代耗尽


def display(cls):
    # 客户代码要求对迭代对象tree 这个生成器进行迭代。
    for cls_name, level in tree(cls):
        # 对树状结构进行排班，不同等级用4位缩进来表示
        indent = ' ' * 4 * level
        print(f'{indent}{cls_name}')


if __name__ == '__main__':
    display(BaseException)
