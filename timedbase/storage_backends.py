from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    """Static storage backend to use with django-storage

    Options:
        location -- path where statis files will be copied
        default_acl -- permissions for copied files
    """
    location = 'static'
    default_acl = 'public-read'

class PublicMediaStorage(S3Boto3Storage):
    """Media storage backend to use with django-storage

    Options:
        location -- path where media files will be copied
        default_acl -- permissions for copied files
        file_everwrite -- Wether to overwrite files or create a new ones
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False