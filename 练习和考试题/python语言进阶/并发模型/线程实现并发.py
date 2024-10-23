# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_THREAD_TOP[]
import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:  # <1>
    """
    指针循环实现函数
    """
    for char in itertools.cycle(r'\|/-'):  # 一个无限循环
        status = f'\r{char} {msg}'  # 拼装想要展示给终端用户的打印信息
        print(status, end='', flush=True)
        if done.wait(.3):  # 堵塞并等待其他线程完成任务并返回True，否则结果默认Flase
            # 这里的0.1表示每0.1秒堵塞一次，所以相当在控制循环的刷新频率
            break  # <5>

    # 跳出循环后清空持续打印的指针和打印的信息。
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')  # <6>


def slow() -> int:
    """
    堵塞函数
    """
    time.sleep(3)  # <7>
    return 42


# end::SPINNER_THREAD_TOP[]

# tag::SPINNER_THREAD_REST[]
def supervisor() -> int:  # <1>
    """
    主程序
    """
    done = Event()  # <2>
    spinner = Thread(target=spin, args=('thinking!', done))  # 将启动一个新的线程运行spin，并在wait堵塞后，调用slow。
    print(f'spinner object: {spinner}')  # 打印spinner对象，输出是<Thread(Thread-1 (spin), initial)> initial是线程的状态
    spinner.start()  # 线程启动，并wait堵塞。
    result = slow()  # 调用slow，并获取结果值。期间spin中的指针动画持续在循环。
    done.set()  # 将wait的结果设为True，表示堵塞结束。spin将跳出循环
    spinner.join()  # 等待spin结束
    return result


def main() -> None:
    result = supervisor()  # <9>
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
# end::SPINNER_THREAD_REST[]
