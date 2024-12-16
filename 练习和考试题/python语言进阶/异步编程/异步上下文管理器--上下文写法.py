from asyncio import Future

import asyncio
from typing import AsyncContextManager


async def task(n):
    print(f"Task {n} started")
    if n == 1:
        raise Exception(f"Task {n} failed")
    await asyncio.sleep(n)
    print(f"Task {n} completed")
    return f"Result of task {n} is successed"


async def rollback(future, exc_type, exc_val, exc_tb):
    print(f"Rolling back {future} due to {exc_type},msg:{exc_val}")
    if await asyncio.sleep(10) is None:  # 模拟处理roll的过程消耗的时间
        print("Rolling back done!")
        return True  # rollback成功，返回True阻止异常进一步扩散
    else:
        return False  # rollback失败，则抛出异常


class Asynccontent(AsyncContextManager):
    def __init__(self, future: Future):
        """
        future是从as_completed(coros)中迭代出来的结果对象
        """
        self.future = future
        super().__init__()

    async def __aenter__(self):
        """
        返回上下文对象自身，用于给as赋值
        使as后的变量等于该类的实例化对象
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """如果发生异常，进行回滚等处理"""
        # aexit无论如何都会在结束时运行，且如果中途发生异常。立刻执行aexit(exc_type, exc_val, exc_tb)
        # 无异常则执行aexit(None, None, None)
        # 所以判断exc_type是否有值，有值则代表需要做rollback处理
        if exc_type:
            if await rollback(self.future, exc_type, exc_val, exc_tb):
                return True  # rollback返回成功，则阻止异常传播


async def main():
    # 创建协程对象列表
    coros = [task(n) for n in range(3)]

    for future in asyncio.as_completed(coros):
        # 用异步上下文替代try:finnaly结构
        async with Asynccontent(future) as Future:
            result = await Future.future
            print(result)

# 运行事件循环
asyncio.run(main())
