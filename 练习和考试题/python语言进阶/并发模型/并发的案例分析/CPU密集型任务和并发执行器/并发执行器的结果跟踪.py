from concurrent.futures import ThreadPoolExecutor, as_completed

import time


def task(n):
    """
    模拟任务
    当n==3时会失败
    其他情况sleep2秒来模拟处理时间
    """
    if n == 3:
        raise ValueError("An error occurred in task 3")

    time.sleep(2)
    return f"Task {n} completed"


with ThreadPoolExecutor(max_workers=3) as executor:
    # 通过executor.submit提交并发任务
    # 并将其返回的Executor对象构建为一个可迭代对象worklist
    worklist = [executor.submit(task, i) for i in range(5)]

    # 循环迭代as_completed(iterable)获取work，并获取其任务的结果
    for work in as_completed(worklist):
        try:
            result = work.result()  # 获取任务结果
            print(result)
        except Exception as e:
            print(f"Task failed with exception: {e}")
