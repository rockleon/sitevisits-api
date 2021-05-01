"""
Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import json
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

SETTINGS_DIR = Path(__file__).resolve().parent
CONFIG_DIR = SETTINGS_DIR.parent
PROJECT_DIR = CONFIG_DIR.parent
APPS_DIR = PROJECT_DIR / 'sitevisits'

# READ SECRETJSON FILE
# SECRETS_FILE = str(SETTINGS_DIR / 'secrets.json')
# if os.path.exists(SECRETS_FILE) is False:
#     raise ImproperlyConfigured(" Please add 'secrets.json' file in config/ folder.")

# with open(SECRETS_FILE) as f:
#     secrets = json.loads(f.read())


# def get_secret(setting, secrets=secrets):
#     '''get the secret variable value of return exception'''
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_message = 'Set the {0} environment variable'.format(setting)
#         raise ImproperlyConfigured(error_message)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# SECRET_KEY = get_secret('SECRET_KEY')
SECRET_KEY = "o&t9*wdcbj(^@=_hr@+n!+xdahv39@m##-hx!*iptw*=ij)-6@"

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
]



THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'rest_auth',
]

LOCAL_APPS = [
    'sitevisits.common',
    'sitevisits.access',
    'sitevisits.account',
]

INSTALLED_APPS = DJANGO_APPS  + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(CONFIG_DIR / 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': get_secret('PG_DATABASE_NAME'),
        # 'USER': get_secret('PG_DATABASE_USER'),
        # 'PASSWORD': get_secret('PG_DATABASE_PASSWORD'),
        # 'HOST': get_secret('PG_DATABASE_HOST'),
        # 'PORT': get_secret('PG_DATABASE_PORT'),
    # }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    str(CONFIG_DIR / 'static'),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = str(CONFIG_DIR / 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = str(APPS_DIR / 'media')
MEDIA_URL = '/media/'



# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTION"
)
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'xsrfheadername',
    'xsrfcookiename',
    'x-devtools-emulate-network-conditions-client-id'
)



# REST-AUTH SETTINGS
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication'
    # ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'
}

API_VERSION = 'v1'

AUTH_USER_MODEL = 'access.User'

# SITE_ID = 3