from .base import *
import os


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timedbase_dev',
        'USER': 'masteruser',
        'PASSWORD': '6Ecs5VeQPit3tPg',
        'HOST': 'database-dev-postgre.czpiepobbs8m.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

AWS_ACCESS_KEY_ID = 'AKIAZFN4FUN2LVTBASG4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'timedbase'
AWS_S3_REGION_NAME = 'us-east-2'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = '{}.s3.{}.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATIC_LOCATION = 'static'
PUBLIC_MEDIA_LOCATION = 'media'

STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATIC_LOCATION)
MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)

AWS_S3_FILE_OVERWRITE = False

STATICFILES_STORAGE = 'timedbase.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'timedbase.storage_backends.PublicMediaStorage'

THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
