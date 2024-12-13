import asyncio


async def task(n):
    if n == 1:
        raise Exception

    print(f"Task {n} started")
    await asyncio.sleep(n)
    print(f"Task {n} completed")
    return f"Result of task {n}"


async def rollback(coro):
    await asyncio.sleep(10)
    print(coro)


async def main():
    coros = [task(n) for n in range(3)]  # 创建协程对象列表
    for coro in asyncio.as_completed(coros):  # 触发事件循环并按完成顺序执行
        try:
            result = await coro
        except:
            await rollback(coro)
        else:
            print(result)


# 运行事件循环
asyncio.run(main())
