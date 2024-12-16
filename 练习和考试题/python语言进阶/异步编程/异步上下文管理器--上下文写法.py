from asyncio import Future

import asyncio
from typing import AsyncContextManager, Coroutine


async def task(n):
    print(f"Task {n} started")
    if n == 1:
        # 模拟任务1失败了
        raise Exception(f"Task {n} failed")
    await asyncio.sleep(n)  #模拟程序运行的消耗时间
    print(f"Task {n} completed")
    return True


async def rollback(future: Future, exc_type, exc_val, exc_tb):
    print(f"Rolling back {future} due to {exc_type},msg:{exc_val}")
    if await asyncio.sleep(.5) is None:  # 模拟处理roll的过程消耗的时间
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
                print(f"Rolling back {self.future} done!")
            else:
                print(f"Rolling back {self.future} failed!")
            return True


async def main():
    count = 0
    # 创建协程对象列表
    coros: list[Coroutine] = [task(n) for n in range(3)]  # 创建协程对象列表

    for future in asyncio.as_completed(coros):
        # 用异步上下文替代try:finnaly结构
        async with Asynccontent(future) as Future:
            if await Future.future:
                count += 1

    print(f"Successed task:{count}")

# 运行事件循环
asyncio.run(main())
