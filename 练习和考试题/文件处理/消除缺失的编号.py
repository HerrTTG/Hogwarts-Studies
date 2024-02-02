#对指定路径下指定的后缀文件的编号进行检查，并且补充修改文件名补充其编号

import os
import re
import shutil

def eliminate_missing_numbers(folder, prefix):  # 编写消除缺失编号的函数，参数folder为绝对路径，参数prefix为文件编号前的前缀
    numbers = []  # 列表numbers记录文件名的编号部分
    files_types = []  # 列表files_types记录文件名的文件类型即后缀部分
    real_filenames = []  # 列表real_filenames记录原始文件名
    prefix_regex = re.compile(r'^(%s)(\d*\d*\d)(.png)$' % prefix)  # 正则表达式匹配带指定前缀的文件名，第2组匹配编号部分，第3组匹配文件类型部分
    filenames = os.listdir(folder)  # 取得路径下文件名及文件夹名的列表
    for filename in filenames:  # 遍历路径下文件名及文件夹名的列表
        if os.path.isfile(os.path.join(folder,filename)):  # 判断是否为文件
            if prefix_regex.search(filename):  # 判断是否匹配正则表达式
                numbers.append(prefix_regex.search(filename).group(2))  # 将匹配文件名的编号部分加入numbers列表
                files_types.append(prefix_regex.search(filename).group(3))  # 将匹配文件名的文件类型部分加入files_types列表
                real_filenames.append(prefix_regex.search(filename).group())  # 将匹配的文件名加入real_filenames列表
    numbers.sort()  # 将numbers列表排序
    for i in range(len(numbers)):  # 循环列表长度的次数
        numbers[i] = i + int(numbers[0])  # 消除缺失的编号，算法是0+第一个元素的值。即0+2 1+2 2+2 3+2.... 生成 2 3 4 5...
    for i, j, k in zip(numbers, files_types, real_filenames):
        after_filefolder = os.path.join(folder, prefix + str(i).rjust(3, '0') + j)  # 组合消除缺失编号后的文件路径，
        # 并且规范编号的格式位为右对齐三位补充0
        befroe_filefolder = os.path.join(folder, k)  # 组合路径+原始文件名
        print('Will rename file {} to {}'.format(befroe_filefolder,after_filefolder))
        #shutil.move(befroe_filefolder, after_filefolder)  # 对文件改名


eliminate_missing_numbers(r'D:\Python\练习和考试题\脱帧图片\640', 'picframe')
