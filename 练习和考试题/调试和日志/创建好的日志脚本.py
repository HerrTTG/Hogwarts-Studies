#!/bin/bash/python3
# -*- encoding: utf-8 -*-
'''
@File    :   loguti.py
@Time    :   2023/07/01 17:14:33
@Author  :   haohe
'''
import logging.config
import os

config = {
    'version':1,
    # 定义格式器
    'formatters':{
        'simple':{
            'format':'%(asctime)s - %(name)s - %(levelname)s -%(message)s',
        },
    },
    # 定义处理器
    'handlers':{
        # 日志输出流
        'console':{
           'class':'logging.StreamHandler',
           'level':'WARNING',
           'formatter':'simple'
        },
        # 日志文件切割,默认保存10天日志
        'file':{
           'class':'logging.handlers.TimedRotatingFileHandler',
           'filename':'loging.log',
           'level':'INFO',
           'when':'D',
           'backupConut':10,
           'formatter':'simple'
        },
    },
    # 定义日志器
    'loggers':{
        'consoleLogger':{
            'handlers':['console'],
            'level':'INFO',
        },
        'fileLogger':{
            'handlers':['console','file'],
            'level':'INFO',
        }
    }
}


def getFileLogger(log_file,hours=None,days=None,size=None):
    # 文件储存log方法，支持根据入参来修改日志的分割方式
    log_dir = os.path.dirname(log_file) # 获取目录名称
    if not os.path.exists(log_dir):
        os.makedirs(log_dir) # 创建目录
    if log_file:
        file_info = {
           'class':'logging.handlers.TimedRotatingFileHandler',
           'filename':log_file,
           'level':'INFO',
           'when':'D',
           'backupCount':10,
           'formatter':'simple'
        }
    if hours:
        file_info["when"] = "H"
        file_info["backupCount"] = hours
    if days:
        file_info["when"] = "D"
        file_info["backupCount"] = days
    if size:
        file_info['class'] = 'logging.handlers.RotatingFileHandler'
        file_info['maxBytes'] = 1024*1024*size
    config['handlers']['file'] = file_info
    logging.config.dictConfig(config=config)
    return logging.getLogger('fileLogger')

#控制台展示log方法，直接调用默认配置好的config
def getConsoleLogger():
    logging.config.dictConfig(config=config)
    return logging.getLogger('fileLogger')

if __name__ == '__main__':
    #判断你的模块代码是不是被当作最顶层模块在使用
    logger = getFileLogger('D:\\Python\\练习和考试题\\调试和日志\\test.log',days=1)
    logger.info('test')
