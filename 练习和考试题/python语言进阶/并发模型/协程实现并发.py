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
            await asyncio.sleep(.3)  # <2>与进程线程不同，使用此语法。暂停时不阻塞其他协程。不能使用time.sleep()
        except asyncio.CancelledError:  # <3>捕获异常，退出循环
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow() -> int:
    await asyncio.sleep(3)  # <4>也是用asyncio.sleep替代time.sleep
    return 42


# end::SPINNER_ASYNC_TOP[]

# tag::SPINNER_ASYNC_START[]
def main() -> None:  # <1> 唯一的常规函数，其他都是协程。
    result = asyncio.run(supervisor())  # <2>asyncio.run这个函数启动协程事件循环，驱动这个协程。最终启动其他协程。
    # main函数保持堵塞，直到supervisor返回值。supervisor的返回值也将变成asyncio.run的返回值，最种赋值给result。
    print(f'Answer: {result}')


async def supervisor() -> int:  # <3>
    spinner = asyncio.create_task(spin('thinking!'))  # <4>创建一个协程Task实例，并最终执行。
    # 这个调用不终止当前协程，当前协程与开启的协程Task并发。
    print(f'spinner object: {spinner}')  # <5><Task pending name='Task-2' coro=<spin() running at ...>>
    result = await slow()  # <6>await 关键字调用slow ，并阻塞当前协程supervisor，直到slow返回。
    spinner.cancel()  # <7>让spin协程抛出CancelledError 配合spin函数中的try进行异常捕获，终止spin协程。
    return result


if __name__ == '__main__':
    main()
# end::SPINNER_ASYNC_START[]
