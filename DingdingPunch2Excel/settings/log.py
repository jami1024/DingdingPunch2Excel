#!/usr/bin/env python3
# coding=utf-8

import os
import sys
from .base import env, ROOT_DIR

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ssss = os.path.dirname(BASE_DIR + '/settings')
# print('ss', ssss)
sys.path.append(os.path.dirname(BASE_DIR + '/settings'))

# if not os.path.isdir(BASE_DIR + '/logs'):
#     os.mkdir(BASE_DIR + '/logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module}.{funcName} {lineno:03d} {process:d} {thread:d} => {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG' if env.bool('DEBUG') else env.str('DJANGO_LOG_LEVEL').upper(),
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        'file': {
            'level': 'DEBUG' if env.bool('DEBUG') else env.str('DJANGO_LOG_FILE_LEVEL').upper(),
            'class': 'DingdingPunch2Excel.settings.MultiCompatibleTimedRotatingFileHandler',
            'encoding': 'UTF-8',
            'filename': ROOT_DIR.path('logs/django.log'),
            'when': "MIDNIGHT",
            'backupCount': 60,
            'interval': 1,
            'formatter': 'verbose'
        },
#
    },
    'loggers': {
        # '': {
        #     'handlers': ['console', 'file'],
        #     'level': 'DEBUG' if env.bool('DEBUG') else env.str('DJANGO_LOG_LEVEL').upper(),
        # },
        # 'django': {
        #     'handlers': ['console', 'file'],
        #     'level': 'DEBUG' if env.bool('DEBUG') else env.str('DJANGO_LOG_LEVEL').upper(),
        #     'propagate': True,
        # },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if env.bool('DEBUG') else 'ERROR',
            'propagate': True,
        },
        'myLog': {
            'handlers': ['console', 'file',],
            'level': 'DEBUG' if env.bool('DEBUG') else env.str('DJANGO_LOG_LEVEL').upper(),
            'propagate': True
        }
    },
}
