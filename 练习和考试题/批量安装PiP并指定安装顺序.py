###目标路径下存放一批whl离线包，
# 且互相之间有依赖关系，
# 该脚本的作用是批量安装，且指定安装顺序，解决依赖关系问题

import glob
import os
import subprocess

whl_dir = r"D:\hzy\paramiko_offline"
whl_files = glob.glob(os.path.join(whl_dir, "*.whl"))

# 安装顺序指定
priority_order = {
    "pycparser": 0,
    "cffi": 1,
    "cryptography": 2,
    "pynacl": 2,  # 并列优先级
    "bcrypt": 3,
    "paramiko": 4,
    "scp": 5
}


# 提取包名（不区分大小写）并排序
def get_pkg_name(path):
    fname = os.path.basename(path)
    return fname.split('-')[0].lower()  # 提取包名部分


# 排序
sorted_paths = sorted(whl_files, key=lambda p: priority_order.get(get_pkg_name(p), 999))

for whl in sorted_paths:
    print(f"Installing {whl} ...")
    subprocess.run(["pip", "install", whl])
