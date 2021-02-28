import logging
from logging.config import fileConfig
from logging.config import dictConfig

def configure_logger(name, log_path="logfile.log"):
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s \n',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': log_path,
                'maxBytes': 64 * 1024 * 1024, # 64 MB
                'backupCount': 10
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'propagate': False,
                'handlers': ['console', 'file'],
            },
            'default': {
                'level': 'DEBUG',
                'propagate': False,
                'handlers': ['console', 'file'],
            },
        },
    })

    return logging.getLogger(name)

logger = configure_logger('default')
