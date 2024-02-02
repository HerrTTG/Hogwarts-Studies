#!/bin/bash/python3
# -*- encoding: utf-8 -*-
'''
@File    :   1.logging模块的基础使用.py
@Time    :   2023/06/26 17:25:45
@Author  :   haohe
'''
import logging

# 创建logger对象,即日志内容中的名称
logger = logging.getLogger('mylogger')
#设置日志等级
logger.setLevel(logging.DEBUG)

# 创建FileHandler对象，即日志生成的文件名
fh = logging.FileHandler('D:\\Python\\练习和考试题\\调试和日志\\mylog.log')
fh.setLevel(logging.DEBUG)

# 创建Formatter对象，即日志的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 将FileHandler对象添加到Logger对象中
logger.addHandler(fh)

# 记录日志信息
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
