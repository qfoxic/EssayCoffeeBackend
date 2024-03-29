"""
Django settings for transport project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#BASE_DIR = '/var/www'
PROJECT_DIR = os.path.join(BASE_DIR, 'transport')
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_w$x2+-q7hk1)4h6)w^pf(8&n3+dmi^hbc4_6_o+-)wfe&9!+*'

CSRF_COOKIE_NAME = 'csrfe'
SESSION_COOKIE_NAME = 'sesse'
#CSRF_COOKIE_DOMAIN = '.customers.yourseller.net'
#SESSION_COOKIE_DOMAIN = '.customers.yourseller.net'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'general',
    'history',
    'msgs',
    'userprofile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userprofile.getuser.ThreadLocals'
)

AUTHENTICATION_BACKENDS = (
    'userprofile.auth.UserProfileBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

FTP_DATA = ('127.0.0.1', 21, 'ftpuser', '(a@4=4ab=b@4)')

DEFAULT_FILE_STORAGE = (
    'ftpstorage.storage.FTPStorage'
)

ROOT_URLCONF = 'editor_urls'

WSGI_APPLICATION = 'editor_wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'transport',
        'USER': 'transport',
        'PASSWORD': 'Secret677',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, 'templates'),)
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

ACTIVE_GROUP = 'editor'
CUSTOM_USER_MODEL = 'userprofile.UserProfile'
