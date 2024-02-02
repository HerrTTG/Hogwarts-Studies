#!/bin/bash/python3
# -*- encoding: utf-8 -*-
'''
@File    :   9.Logging模块的使用案例.py
@Time    :   2023/06/28 18:26:55
@Author  :   haohe
'''
"""
    日志需求:
        1要求将所有级别的所有日志都写入磁盘文件中
        2all.log文件中记录所有的日志信息,日志格式为：日期和时间 - 日志级别 - 日志信息
        3error.log文件中单独记录error及以上级别的日志信息,日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
        4要求all.log在每天凌晨进行日志切割
"""
import logging
from logging import handlers
import datetime

# 创建日志记录器
logger = logging.getLogger('mylog')

# 设置all.log文件的日志最低级别为DEBUG
logger.setLevel(logging.DEBUG)
# 创建一个格式化器
formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s')

# 创建一个日志切割器
All_Handler =  logging.handlers.TimedRotatingFileHandler(filename='D:\\Python\\练习和考试题\\调试和日志\\all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# filename:日志文件名称,when:指定文件的切割时间间隔,可选值为S(秒),M(分钟),H(小时),D(天),W0-W6(周一至周日),midnight(每天凌晨)
# backupCount:指定保留的日志文件数量
# interval:指定切割时间间隔的数量
All_Handler.setLevel(logging.DEBUG)
All_Handler.setFormatter(formatter1)

# 创建一个文件查看器
Error_Handler = logging.FileHandler('D:\\Python\\练习和考试题\\调试和日志\\error.log')
Error_Handler.setLevel(logging.ERROR)
Error_Handler.setFormatter(formatter2)

logger.addHandler(All_Handler)
logger.addHandler(Error_Handler)

# 发送日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
