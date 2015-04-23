from settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'circleci_test',
        'USER': 'ubuntu',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
