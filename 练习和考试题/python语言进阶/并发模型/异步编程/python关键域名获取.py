#!/usr/bin/env python3
"""
获取python关键字注册的域名,如await.dev

"""
import asyncio
import socket
from keyword import kwlist


# MAX_KEYWORD_LEN = 4  # <1>


async def probe(domain: str) -> tuple[str, bool]:  # <2>
    loop = asyncio.get_running_loop()  # <3>一个协程库的事件循环
    try:
        await loop.getaddrinfo(domain, None)  # <4>将getaddrinfo这个方法使用事件循环调用，
        # 相当于把该工作加入事件循环。等待协程事件安排工作。并在工作启动后，使用await抛出控制权，交由事件循环。
        # 直到工作结束
        # 该表达式无需方法返回值，抛出异常则表示域名不可达。
    except socket.gaierror:
        return (domain, False)
    else:
        return (domain, True)


async def main() -> None:  # <5>
    names = (kw for kw in kwlist)  # <6>从python关键字列表中获取关键字
    domains = (f'{name}.dev'.lower() for name in names)  # <7>拼接为域名
    coros = [probe(domain) for domain in domains]  # <8>调用probe并传入domain，构造一个列表来储存协程对象
    for coro in asyncio.as_completed(coros):  # <9>as_completed按照完全的顺序生成协程。
        domain, found = await coro  # <10> 这里await的作用是获取coro的返回值而不是等待堵塞，
        # 前面as_completed 已经在等待协程完成了。所以await不会堵塞赋值动作。
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())  # <11>
