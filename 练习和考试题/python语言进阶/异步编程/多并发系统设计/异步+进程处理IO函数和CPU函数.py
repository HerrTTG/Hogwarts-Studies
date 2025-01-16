from concurrent.futures import ProcessPoolExecutor

import aiofiles  # 异步文件操作库
import asyncio


# CPU 密集型计算函数
def compute(data: list) -> int:
    # 模拟复杂计算（如统计、处理数据等）
    result = sum(int(x) for x in data if x.isdigit())
    return result


# 异步读取文件函数
async def read_file(filepath, chunk_size=1024) -> list:
    print(f"Reading file: {filepath}")
    results = []

    # 异步打开文件
    async with aiofiles.open(filepath, mode='r') as f:
        while content := await f.read(chunk_size):
            results.append(content.split(","))
    return results


# 处理单个文件任务
async def process_file(filepath, executor: ProcessPoolExecutor) -> int:
    # 文件读取这种IO操作，交给异步操作
    # 异步读取文件
    datas = await read_file(filepath)

    # 数据计算式CPU密集型，所以交给多进程或者多线程
    # 使用 executor.map 指定其计算总和
    # executor.map会等待任务完成（这是一个阻塞操作），因此当前协程函数会暂停。
    # 但这种阻塞仅影响当前协程，其它协程函数仍然可以被事件循环调度
    results = executor.map(compute, datas)  # 批量调度计算任务
    total = sum(results)

    # # 汇总结果
    # return filepath,total
    print(f"Total for {filepath}: {total}")
    return total


# 主程序
async def main(filepaths, procs):
    # 使用指定进程数的 ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=procs) as executor:
        # 创建协程任务
        tasks = [process_file(filepath, executor) for filepath in filepaths]
        # 加入事件循环启动
        # 注意gather是根据加入事件循环的顺序来返回结果的，而不是完成顺序
        results = await asyncio.gather(*tasks)

    # 输出最终结果

    # grand_total=0
    # for file,total in results:
    #     print(f"Total for {file}: {total}")
    #     grand_total+=total

    grand_total = sum(results)
    print(f"Grand total for all files: {grand_total}")


if __name__ == "__main__":
    # 模拟文件路径
    filepaths = [f"file_{i}.txt" for i in range(1, 6)]  # 假设有 5 个文件

    # 指定进程数
    procs = 4  # 根据 CPU 核心数或任务需求调整

    # 运行主程序
    asyncio.run(main(filepaths, procs))
