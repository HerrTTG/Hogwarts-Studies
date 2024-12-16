import asyncio


async def task(n):
    print(f"Task {n} started")
    await asyncio.sleep(n)
    print(f"Task {n} completed")
    return f"Result of task {n}"


async def rollback(exc_type, exc_val, exc_tb):
    print(f"Rolling back due to {exc_val}")
    await asyncio.sleep(1)
    if exc_type is Exception:
        return True  # 处理异常并阻止传播


class AsyncCompleted:
    def __init__(self, iterable):
        self.iterable = iterable

    async def __aenter__(self):
        """返回上下文对象"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """如果发生异常，进行回滚等处理"""
        if exc_type:
            if await rollback(exc_type, exc_val, exc_tb):
                return True  # 阻止异常传播

    async def __aiter__(self):
        """
        对上下文对象进行迭代，则返回一个异步生成器
        从asyncio.as_completed(self.iterable)中迭代，并await结果
        用yield返回结果
        """
        for coro in asyncio.as_completed(self.iterable):
            yield await coro


async def main():
    # 创建协程对象列表
    coros = [task(n) for n in range(3)]

    # 使用异步上下文管理器
    async with AsyncCompleted(coros) as completed:
        # 遍历 completed，它是异步迭代器__aiter__
        async for result in completed:
            print(result)


# 运行事件循环
asyncio.run(main())
