#!/bin/bash/python3
# -*- encoding: utf-8 -*-
'''
@File    :   12.Logging模块调用写好的日出处理脚本.py
@Time    :   2023/07/01 17:43:51
@Author  :   haohe
'''
from 创建好的日志脚本 import getFileLogger
# 配置日志
logger = getFileLogger('D:\\Python\\练习和考试题\\调试和日志\\testD.log',days=1)

# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
