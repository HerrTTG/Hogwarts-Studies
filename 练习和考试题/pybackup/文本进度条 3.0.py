# 文本进度条完整版

import time

scale = 50
# scale在这里其实是打印【】的行的宽度，并且循环的计数
print("执行开始".center(scale + 10, "-"))
start = time.perf_counter()
for i in range(scale):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{0:^3.0f}%[{1}->{2}]{3:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n" + "执行结束".center(scale + 10, "-"))
