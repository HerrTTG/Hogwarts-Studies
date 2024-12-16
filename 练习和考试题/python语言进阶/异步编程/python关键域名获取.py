#!/usr/bin/env python3
"""
获取python关键字注册的域名,如await.dev

"""
import asyncio
import socket
from keyword import kwlist


# MAX_KEYWORD_LEN = 4  # <1>


async def probe(domain: str) -> tuple[str, bool]:  # <2>
    loop = asyncio.get_running_loop()  # <3>一个协程库的事件循环，在这里赋值引用是为了后面使用getaddrinfo这个方法。
    try:
        await loop.getaddrinfo(domain, None)
        # 协程方法asyncio库自带的，
        # 前面引用loop也是为了该方法，没什么特别的，只是无需再自己定义sync def 去写一个协程函数来执行域名获取的行为了。
    except socket.gaierror:
        # 该表达式无需方法返回值，抛出异常则表示域名不可达。
        return (domain, False)
    else:
        return (domain, True)


async def main() -> None:  # <5>
    """
    main函数也必须是一个协程，
    因为要在函数中使用await或者asyncio.as_completed等关键字。来堵塞主程序
    """
    names = (kw for kw in kwlist)  # <6>从python关键字列表中获取关键字
    domains = (f'{name}.dev'.lower() for name in names)  # <7>拼接为域名

    coros = [probe(domain) for domain in domains]
    # <8>迭代domains并调用probe并传入domain，注意调用协程函数probe，并不会让协程函数执行，而是返回协程对象。
    # 构造一个列表来储存协程对象

    for coro in asyncio.as_completed(coros):
        # <9>as_completed(coros)会触发coros中的协程对象进入事件循环
        # 注意，as_completed返回一个迭代器,每次迭代返回一个完成的协程的结果，按照完成顺序返回结果，而不是根据传入时间循环的协程对象来返回。
        # 能被as_completed返回结果的协程对象，一定已经完成。

        domain, found = await coro  # <10> 这里await的作用是获取coro的返回值而不是等待堵塞，
        # 前面as_completed 已经在等待协程完成了。所以await不会堵塞赋值动作，会立刻将结果赋值。
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())  # <11>启动整个事件循环
