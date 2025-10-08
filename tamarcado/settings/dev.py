from tamarcado.settings.base import *

ALLOWED_HOSTS = []
DEBUG = True
LOGGING = {
    **LOGGING,
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
        }
    }
}