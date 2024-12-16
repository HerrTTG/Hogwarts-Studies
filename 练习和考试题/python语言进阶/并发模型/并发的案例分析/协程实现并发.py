# spinner_async.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_ASYNC_TOP[]
import asyncio
import itertools


async def spin(msg: str) -> None:  # <1>
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')

        try:
            await asyncio.sleep(.3)  # <2>与进程线程不同，不能使用其他的wait方法或者sleep来控制刷新率
            # 必须使用await 关键字+协程特有的asyncio.sleep(.3),才能在堵塞本函数的情况下释放出去执行别的函数。
        except asyncio.CancelledError:  # <3>捕获异常，退出循环
            # 结束的方法与进程线程也不同，直接捕获asyncio.CancelledError异常。
            # 注意，只有task启动的协程，可以使用task.cancel()
            break

    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow() -> int:
    await asyncio.sleep(3)  # <4>也是用asyncio.sleep替代time.sleep。
    # 来模拟需要等待3秒，才能返回结果
    # 必须使用await关键字+协程特有的asyncio.sleep(3),才能在堵塞本函数的情况下释放出去执行别的函数。
    # 使用time.sleep 会整体堵塞
    return 42


async def supervisor() -> int:  # <3>
    spinner = asyncio.create_task(spin('thinking!'))  # <4>创建一个协程Task实例，并最终交由事件循环调度执行。
    # 这个执行不会堵塞当前代码块，当前代码块与新开启的协程Task spinner并发。
    print(f'spinner object: {spinner}')  # <5><Task pending name='Task-2' coro=<spin() running at ...>>

    try:
        result = await slow()  # <6>重点await 关键字调用slow，并将slow这个异步函数加入事件循环调度
        # 并阻塞当前代码块，直到slow返回结果。
        # await就是一种显式的、主动放权GIL的行为
        # 当前代码块因此被堵塞
        # 但由当前代码块发起的task和slow不受此处await的影响继续被时间循环调度。
    except:
        ...
    else:
        return result
    finally:
        spinner.cancel()  # <7>让spin协程抛出CancelledError 配合spin函数中的try进行异常捕获，终止spin协程。
        # 注意，只有task启动的协程，可以使用task.cancel()
        # await关键字拉起的协程无法被取消


def main() -> None:  # <1> 唯一的常规函数，其他都是协程。
    """
    该常规函数用于启动协程事件池，
    并堵塞当前程序
    """
    result = asyncio.run(supervisor())  # <2>asyncio.run这个函数启动协程事件循环，驱动这个协程。最终启动其他协程。
    # main函数保持堵塞，直到supervisor返回值。supervisor的返回值也将变成asyncio.run的返回值，最终赋值给result。
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
# end::SPINNER_ASYNC_START[]
