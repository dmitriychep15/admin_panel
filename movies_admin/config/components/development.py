'''Quick-start development settings - unsuitable for production.'''

import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ('127.0.0.1', '0.0.0.0', 'localhost')

# For django_debug_toolbar
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost')
