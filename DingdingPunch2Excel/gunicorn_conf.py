#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import logging
# import logging.handlers
# from logging.handlers import WatchedFileHandler
# import os
# import multiprocessing

bind = "127.0.0.1:50055"
backlog = 128
timeout = 3600
chdir = '/data1/DingdingPunch2Excel'
worker_class = 'gevent' #使用gevent模式，还可以使用sync 模式，默认的是sync模式
workers = 8  # multiprocessing.cpu_count()    #进程数
threads = 4  # multiprocessing.cpu_count()*4 #指定每个进程开启的线程数

logconfig_dict = {
    'version':1,
    'disable_existing_loggers': False,
    'loggers':{
        "gunicorn.error": {
            "level": "ERROR",# 打日志的等级可以换的，下面的同理
            "handlers": ["error_file"],  # 对应下面的键
            "propagate": 1,
            "qualname": "gunicorn.error"
        },

        "gunicorn.access": {
            "level": "DEBUG",
            "handlers": ["access_file"],
            "propagate": 0,
            "qualname": "gunicorn.access"
        }
    },
    'handlers':{
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024*1024*1024,# 打日志的大小，我这种写法是1个G
            "backupCount": 1,# 备份多少份，经过测试，最少也要写1，不然控制不住大小
            "formatter": "generic",# 对应下面的键
            # 'mode': 'w+',
            "filename": "/tmp/logs/gunicorn.error.log"# 打日志的路径
        },
        "access_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024*1024*1024,
            "backupCount": 1,
            "formatter": "generic",
            "filename": "/tmp/logs/gunicorn.access.log",
        }
    },
    'formatters':{
        "generic": {
            "format": "'[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s'", # 打日志的格式
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",# 时间显示方法
            "class": "logging.Formatter"
        },
        "access": {
            "format": "'[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s'",
            "class": "logging.Formatter"
        }
    }
}


proc_name = 'ding_api'   #进程名