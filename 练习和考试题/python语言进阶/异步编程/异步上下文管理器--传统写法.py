import asyncio

async def task(n):
    print(f"Task {n} started")
    if n == 1:
        raise Exception(f"Task {n} failed")
    await asyncio.sleep(n)
    print(f"Task {n} completed")
    return f"Result of task {n} is successed"


async def rollback(future, exc):
    if await asyncio.sleep(10) is None:
        print(f"Rolling back {future} due to {type(exc)},msg:{exc}")
    else:
        raise exc


async def main():
    coros = [task(n) for n in range(3)]  # 创建协程对象列表
    for future in asyncio.as_completed(coros):  # 触发事件循环并按完成顺序执行
        try:
            result = await future
        except Exception as e:
            await rollback(future, e)
        else:
            print(result)


# 运行事件循环
asyncio.run(main())
