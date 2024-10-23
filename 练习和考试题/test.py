async def slow() -> int:
    await asyncio.sleep(3)  # <4>也是用asyncio.sleep替代time.sleep
    return 42


async def supervisor() -> int:  # <3>
    spinner = asyncio.create_task(spin('thinking!'))  # <4>创建一个协程Task实例，并最终执行。
    # 这个调用不终止当前协程，当前协程与开启的协程Task并发。
    print(f'spinner object: {spinner}')  # <5><Task pending name='Task-2' coro=<spin() running at ...>>
    result = await slow()  # <6>await 关键字调用slow ，并阻塞当前协程supervisor，直到slow返回。
    spinner.cancel()  # <7>让spin协程抛出CancelledError 配合spin函数中的try进行异常捕获，终止spin协程。
    return result
