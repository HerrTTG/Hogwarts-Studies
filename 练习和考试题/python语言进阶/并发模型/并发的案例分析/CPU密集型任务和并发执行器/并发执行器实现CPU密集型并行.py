#!/usr/bin/env python3

"""
procs.py: shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.
"""
import math


PRIME_FIXTURE = [
    (2, True),
    (142702110479723, True),
    (299593572317531, True),
    (3333333333333301, True),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),
]

NUMBERS = [n for n, _ in PRIME_FIXTURE]


# tag::IS_PRIME[]
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


# end::IS_PRIME[]


# tag::PRIMES_PROC_TOP[]
from time import perf_counter
from typing import NamedTuple
from concurrent import futures
from multiprocessing import cpu_count


class PrimeResult(NamedTuple):  # <3>
    """
    结果对象的元组模型设计
    """
    n: int  # 计算的数
    prime: bool  # 结果
    elapsed: float  # 耗时


def check(n: int) -> PrimeResult:  # <6>
    """
    子线程执行的任务函数，
    统计子线程的单独消耗时间，
    调用计算函数计算结果，
    最终返回结果对象
    """
    t0 = perf_counter()  # 记录开始时的时间戳
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)  # 结束是重新获取时间戳，减去开始时的时间戳，获得了消耗的时间。

# tag::PRIMES_PROC_MAIN[]
def main() -> None:
    """
    唯一入口函数，
    使用执行器来托管并发进程的创建和执行，
    并且执行器也无需使用进程池来通讯入参和结果。
    """
    try:
        procs = int(input('输入并行进程数:'))
    except:
        procs = cpu_count()

    # 初始化执行器各项参数
    executor = futures.ProcessPoolExecutor(procs)  # 设置执行器为进程模式，职程变量procs
    # _max_workers属性可获得实际的职程数
    actual_procs = executor._max_workers  # type:ignore
    print(f'Checking {len(NUMBERS)} numbers with {actual_procs} processes:')


    t0 = perf_counter()  # 记录主程序开始时间
    numbers = sorted(NUMBERS, reverse=True)
    with executor:
        # 使用with关键字处理执行器
        for n, prime, elapsed in executor.map(check, numbers):
            # 类似于普通的map功能。返回一个生成器，通过的迭代来获取函数调用的返回值
            # 将numbers这个可迭代对象中的项都去执行check。
            # 这里执行器会自动的根据职程参数来创建子进程去执行。也无需自建进程池来管理输入和输出，
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')

    # with释放后代表所有进程都结束了
    # 主程序计算时间，打印结果
    time = perf_counter() - t0
    print(f'{len(numbers)} checks in {time:.2f}s')

if __name__ == '__main__':
    main()
# end::PRIMES_PROC_MAIN[]
