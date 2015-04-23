import os

from settings.common import *

# Django settings for motiv8_django project in development.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_riot', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'meodog',
        'PASSWORD': 'meo123',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

DATABASES['default']['NAME'] = '{0}_{1}'.format(DATABASES['default']['NAME'], os.environ["LOGNAME"])

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
