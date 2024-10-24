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
from multiprocessing import Process, SimpleQueue, cpu_count  # <1>
from multiprocessing import queues  # <2>


class PrimeResult(NamedTuple):  # <3>
    n: int  # 计算的数
    prime: bool  # 结果
    elapsed: float  # 耗时


# SimpleQueue是一个进程共享的队列
JobQueue = queues.SimpleQueue[int]  # <4>待处理的任务队列模型
ResultQueue = queues.SimpleQueue[PrimeResult]  # <5>结果队列模型


def start_jobs(
        procs: int, jobs: JobQueue, results: ResultQueue  # <11>proces参数是并行检查素数的进程数，如=2则开启两个子进程
) -> None:
    for n in NUMBERS:
        jobs.put(n)  # <12>把要检查的number塞入jobs队列中
    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))  # <13>创建子线程，并将队列传入其中
        proc.start()  # <14>启动子线程
        jobs.put(0)  # <15>每个子线程启动后，都在队列末尾放入一个0，这是“毒药丸”，吃了就停止。


def worker(jobs: JobQueue, results: ResultQueue) -> None:  # <7>多个进程并行调用worker但共享队列
    while n := jobs.get():  # <8>n从jobs队列中取出，并判断n。只要n不为0“毒药丸”，就会循环。
        results.put(check(n))  # <9>调用check(n)获取计算结果，并塞入结果队列results中
    results.put(PrimeResult(0, False, 0.0))  # <10>在队列末尾塞入一个“毒药丸”，表示结束。


def check(n: int) -> PrimeResult:  # <6>
    t0 = perf_counter()  # 记录开始时的时间戳
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)  # 结束是重新获取时间戳，减去开始时的时间戳，获得了消耗的时间。


def report(procs: int, results: ResultQueue) -> int:  # <6>
    checked = 0
    procs_done = 0
    while procs_done < procs:  # <7>子进程不结束，就会无限循环下去
        n, prime, elapsed = results.get()  # <8>从结果序列中解包
        if n == 0:  # <9>n=0说明循环已经到了队列末尾的“毒药丸”，表明某一个进程的队列已经结束了
            procs_done += 1  # 表明完成队列的进程数+1
        else:
            checked += 1  # <10>记录表报打印了多少个数
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked


# end::PRIMES_PROC_TOP[]
# tag::PRIMES_PROC_MAIN[]
def main() -> None:
    try:
        procs = int(input('输入并行进程数:'))
    except:
        procs = cpu_count()
    print(f'Checking {len(NUMBERS)} numbers with {procs} processes:')

    t0 = perf_counter()  # 记录主程序开始时间

    jobs: JobQueue = SimpleQueue()  # <2>实例化待执行任务队列
    results: ResultQueue = SimpleQueue()  # 实例化结果队列

    start_jobs(procs, jobs, results)  # <3>子进程开始任务
    checked = report(procs, results)  # <4>主进程在子进程运行过程中持续报表打印

    elapsed = perf_counter() - t0  # 获取主程序的消耗时长
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':
    main()
# end::PRIMES_PROC_MAIN[]
