from agl_financial_backend.settings.settings_old import ALLOWED_HOSTS
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["localhost", ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "financial_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}



