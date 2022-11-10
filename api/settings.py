"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from pickle import FALSE
from decouple import Config, RepositoryEnv, Csv
# import pymysql
import base64
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_FILE = './config/.env'
getenv = Config(RepositoryEnv(DOTENV_FILE))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w3mtq5$1+y)v%7bsvwm7#8444z8!s^fup5z7z@j+p810n8gfcv'

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = getenv('SECRET_KEY')

DEBUG = getenv('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', default=['*'], cast=Csv())
print(ALLOWED_HOSTS)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'blog',
    'category',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    # 'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    # ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
    # 'USER_DETAILS_SERIALIZER': 'userapp.serializer.UserDetailsSerializer'
    # "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    # 'DATE_FORMAT': "%d-%m-%Y",
    # 'DATETIME_FORMAT': "%d-%m-%Y %H:%M:%S",
}

WSGI_APPLICATION = 'api.wsgi.application'

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8000"
]

CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv('DB_NAME'),  # bHlvbg==
        'USER': getenv('DB_USER'),  # ZGV2U
        'PASSWORD': getenv('DB_PASSW'),  # ZGV2U
        'HOST': getenv('DB_HOST'),  # bG9jYWxob3N0
        'PORT': getenv('DB_PORT'),  # MzMwNg==
        # 'NAME': 'lyon',  # bHlvbg==
        # 'USER': 'root',  # ZGV2U
        # 'PASSWORD': 'root',  # ZGV2U
        # 'HOST': '127.0.0.1',  # bG9jYWxob3N0
        # 'PORT': 3306,  # MzMwNg==
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# STATIC_URL = '/static/'

USE_TZ = False