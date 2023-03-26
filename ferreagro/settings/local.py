from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR, 'static']


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('PASS')
EMAIL_PORT = 587
