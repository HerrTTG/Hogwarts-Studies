# tqdm 第三方库，小巧精致的进度条工具

import tqdm
import time

for i in tqdm.tqdm(range(1, 101)):
    time.sleep(0.01)
