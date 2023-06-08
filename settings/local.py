from .base import *


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('NAME'), 
        'USER': os.environ.get('USER'), 
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'), 
        'PORT': os.environ.get('PORT'),
    }
}