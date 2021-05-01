import django_heroku

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())