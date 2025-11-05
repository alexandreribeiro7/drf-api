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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '0.0.0.0'
EMAIL_PORT = 1025