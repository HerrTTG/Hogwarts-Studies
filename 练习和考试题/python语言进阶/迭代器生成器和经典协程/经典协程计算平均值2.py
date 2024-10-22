from collections.abc import Generator
from typing import NamedTuple


class Result(NamedTuple):
    # 定义一个元组类
    count: int = 0
    avg: float = 0


class Flag():
    # 定义一个哨符
    def __str__(self):
        return f'<Flag>'


def avg(verbool: bool = False) -> Generator[None, float | Flag, Result]:
    # Generator[None, float | Flag, Result]
    # 表示生成器yield不返回任何项,接受float或者Flag类型输入,最后return一个Result类型
    total = 0.0
    count = 0
    avg = 0.0
    while True:
        # 一个无限循环的生成器主体，当且仅当判断到哨符，跳出循环。
        _tmp = yield  # 不返回任何项，只做接收
        if verbool:
            #判断是否需要打印接收到的值
            print(f'received:', _tmp)
        # 判断接收的值是否为哨符，是则跳出循环结束迭代
        if isinstance(_tmp, Flag):
            break
        else:
            total += _tmp
            count += 1
            avg = total / count

    #循环跳出表示结束接收新值，生成器函数返回Result类型。并存在StopIteration的value中
    return Result(count, avg)


def factory():
    # 这也是个生成器
    # 委托avg这个生成器进行迭代
    res = yield from avg(True)
    # print(f'Finished',res)

    # 返回受委托的生成器对象，才能让客户代码for中可以直接使用send方法给avg传值
    return res


if __name__ == '__main__':
    # 此时fn=res=avg(True)
    fn = factory()

    # 实例化Stop变量作为哨符
    Stop = Flag()

    # for循环客户迭代请求。从列表中取值并传入send中
    for v in [None, 10, 20, 30, Stop]:
        try:
            fn.send(v)
        # 拦截抛出的异常。最后打印avg生成器return的值
        except StopIteration as exc:
            print(exc.value)
