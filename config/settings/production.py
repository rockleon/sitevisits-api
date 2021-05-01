import django_heroku

from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())