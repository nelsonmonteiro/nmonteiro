from configs.common.settings import *

WSGI_APPLICATION = 'configs.development.wsgi.application'

PROJECT_DOMAIN = "https://nelsonmonteiro.eu"
ADMINS = (('DJINA Support', 'support@nelsonmonteiro.eu'),)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['127.0.0.1', 'nelsonmonteiro.eu']


### MEDIA AMAZON S3
AWS_S3_ACCESS_KEY_ID = 'AKIAJH6EHIQVQOAOI45A'
AWS_S3_SECRET_ACCESS_KEY = '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'

MEDIA_URL = ''

DEFAULT_FILE_STORAGE = 'apps.core.utils.storage.DefaultFilesStorage'
DEFAULT_FILES_BUCKET = 'nmonteiro-dev-media'
DEFAULT_FILES_DOMAIN = 'd2q6wauuctevkk.cloudfront.net'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nmonteirodev',
        'USER': 'nmonteirodev',
        'PASSWORD': 'Dj#Dev$?161050',
        'HOST': 'nmonteiro-dev.cuznkjxj8uqx.us-west-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}


try:
    from local_settings import *
except ImportError:
    pass
