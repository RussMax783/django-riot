from settings.common import *

# Django settings for motiv8_django project in development.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '[ENTER DB NAME]', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '[ENTER DB USER]',
        'PASSWORD': '[ENTER PASSWORD]',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
