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
]  # 待计算的数的容器

NUMBERS = [n for n, _ in PRIME_FIXTURE]


#忽略元组后的结果，只保留要计算的数


# tag::IS_PRIME[]
def is_prime(n: int) -> bool:
    """
    待并发的计算函数，忽略
    """
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
from multiprocessing import Process, SimpleQueue, cpu_count  # <1>SimpleQueue是一个进程共享的队列 cpu_count是CPU核数计算
from multiprocessing import queues  # <2>SimpleQueue是一个函数，为了定义注释中的类型，需要使用到queues.SimpleQueue


class PrimeResult(NamedTuple):  # <3>定义一个元组类，来设计结果对象的内容。
    n: int  # 计算的数
    prime: bool  # 结果
    elapsed: float  # 耗时


# 注释类型定义
JobQueue = queues.SimpleQueue[int]  # <4>JobQueue对象是一个待处理的任务队列，内部储存类型为int。也就是前面筛选好的NUMBERS
ResultQueue = queues.SimpleQueue[PrimeResult]  # <5>结果队列，储存自定义类型PrimeResult的对象


def start_jobs(procs: int, jobs: JobQueue, results: ResultQueue) -> None:
    """
    子进程开启函数，入口函数
    procs是要并发开起的进程数
    jobs是待处理任务队列
    results是结果队列

    开启并子进程并执行worker(jobs,results)
    """

    for n in NUMBERS:
        jobs.put(n)  # <12>先把要检查的number全部塞入jobs队列中

    for _ in range(procs):
        # 启动指定procs数量的子进程，并执行工作函数worker

        proc = Process(target=worker, args=(jobs, results))  # <13>创建子线程，任务队列和结果队列传入其中
        proc.start()  # <14>启动子线程
        jobs.put(0)  # <15>每个子线程启动后，都在队列末尾放入一个0，这是“毒药丸”，吃了就停止。代表着任务到此结束。
        #假如要开启5个线程，那就会在队末出现5个0。5个进程分别遇到后，分别停止。


def worker(jobs: JobQueue, results: ResultQueue) -> None:
    """
    并发执行的工作函数，
    从任务队列jobs领取任务，
    在调用check函数获取结果，
    将结果写入结果队列results中
    """
    while n := jobs.get():  # <8>从队列中取出一个值，只要不为0“毒药丸”，就会循环。同时将值赋值给n。
        results.put(check(n))  # <9>调用check(n)获取计算结果，并塞入结果队列results中
    else:
        results.put(PrimeResult(0, False, 0.0))  # <10>在队列末尾塞入一个“毒药丸”，表示结束。


def check(n: int) -> PrimeResult:  # <6>
    """
    受worker委托，调用计算素数函数的函数
    计算计算素数的消耗时间，
    将素数的计算结果构造一个PrimeResult对象返回
    """
    t0 = perf_counter()  # 记录开始时的时间戳
    result = is_prime(n)  # 执行计算
    return PrimeResult(n, result, perf_counter() - t0)  # 返回结果


def report(procs: int, results: ResultQueue) -> int:  # <6>
    """
    并发监控函数，
    无限循环直至所有子进程结束。
    在循环中不断从结果序列中获取结果元组
    并实时的打印当前结果池中的计算结果
    返回总共计算了多少个数
    """
    checked = 0
    procs_done = 0
    while procs_done < procs:  # <7>子进程不结束，就会无限循环下去
        n, prime, elapsed = results.get()  # <8>从结果序列中解包元组
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
    """
    主程序，输入或者根据CPU确定并发的进程数。
    统计整体程序运行的时间。

    """
    try:
        procs = int(input('输入并行进程数:'))
    except:
        procs = cpu_count()
    print(f'Checking {len(NUMBERS)} numbers with {procs} processes:')

    t0 = perf_counter()  # 记录主程序开始时间

    jobs: JobQueue = SimpleQueue()  # <2>实例化待执行任务队列
    results: ResultQueue = SimpleQueue()  # 实例化结果队列

    start_jobs(procs, jobs, results)  # <3>创建并执行子进程
    checked = report(procs, results)  # <4>主进程调用report函数，堵塞主程序。
    # report函数无限循环持续从队列中获取结果进行打印。直到所有进程结束。返回结果。

    elapsed = perf_counter() - t0  # 获取主程序的消耗时长
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>


if __name__ == '__main__':
    main()
# end::PRIMES_PROC_MAIN[]
