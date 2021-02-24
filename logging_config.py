
import datetime
import logging
import logging.config


today = datetime.datetime.now()
timestamp = today.strftime('%y%m%d_%H%M%S%z')

logging_config = {

    'version': 1,

    'formatters': {
        'brief': {
            'format': '%(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'brief',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': f'tool_log/verbose_{timestamp}.log',
            'mode': 'a',
            'encoding': 'utf-8',
        },
        'brief_file': {
            'level': 'INFO',
            'formatter': 'brief',
            'class': 'logging.FileHandler',
            'filename': f'tool_log/out_{timestamp}.log',
            'mode': 'w',    # rewrite
            'encoding': 'utf-8',
        }
    },

    'loggers': {
        '': {  # root logger
            'handlers': [
                'console',
                'file',
                'brief_file'
            ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'PIL': {    # logger of Pillow library
            'level': 'WARN',
        }
    }

}

logging.config.dictConfig(logging_config)

root_logger = logging.getLogger()
