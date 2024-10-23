# spinner_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

from multiprocessing import Process, Event  # 与线程的区别仅在此处，multiprocessing.Event是一个函数，返回synchronize.Event
from multiprocessing import synchronize  # 所以要导入的是synchronize.Event

# tag::SPINNER_PROC_IMPORTS[]
import itertools
import time


def spin(msg: str, done: synchronize.Event) -> None:  # <3>
    # end::SPINNER_PROC_IMPORTS[]
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 42


# tag::SPINNER_PROC_SUPER[]
def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))  # 将启动一个全新的python解析器以子进程的形式在后台运行。
    print(f'spinner object: {spinner}')  # <Process name='Process-1' parent=31496 initial> parent是此模块的进程ID
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


# end::SPINNER_PROC_SUPER[]

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
