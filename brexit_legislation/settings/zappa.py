import os

from .base import *  # noqa

ZAPPA_STAGE = os.environ['STAGE']
assert ZAPPA_STAGE in ('dev', 'prod')

FORCE_SCRIPT_NAME = '/'

ALLOWED_HOSTS = [
    'pr9oybf6j5.execute-api.eu-west-1.amazonaws.com',  # Prod
    'eu-regulation.labs.democracyclub.org.uk',  # Prod
]
USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DATABASE_HOST'),
        'USER': os.environ.get('DATABASE_USER'),
        'PORT': '5432',
        'NAME': os.environ.get('DATABASE_NAME'),
        'PASSWORD': os.environ.get('DATABASE_PASS')
    }
}

DEBUG = False

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL': os.environ.get('ES_URL'),
        'INDEX_NAME': 'eu-regulations',
        'TIMEOUT': 2,
    },
}


TMP_ASSETS_ROOT = "/tmp/assets_root"
STATIC_ROOT = '/tmp/static_root/'

# Make the tmp static dirs whenever django is started
os.makedirs(TMP_ASSETS_ROOT, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_FINDERS = (
    'brexit_legislation.s3_lambda_storage.ReadOnlySourceFileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Used by ReadOnlySourceFileSystemFinder
READ_ONLY_PATHS = (
    (root('assets'), TMP_ASSETS_ROOT),  # noqa
)

AWS_S3_SECURE_URLS = True
AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_USE_SSL = False

AWS_STORAGE_BUCKET_NAME = "static.labs.democracyclub.org.uk"
AWS_S3_CUSTOM_DOMAIN = "static.labs.democracyclub.org.uk"

STATICFILES_LOCATION = 'eu-regulation/static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = 'brexit_legislation.s3_lambda_storage.StaticStorage'

MEDIAFILES_LOCATION = 'eu-regulation/media'
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'brexit_legislation.s3_lambda_storage.MediaStorage'

CSRF_TRUSTED_ORIGINS = [
    'eu-regulation.labs.democracyclub.org.uk',
]
