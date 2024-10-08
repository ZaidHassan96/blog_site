"""
Django settings for my_site project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
from os import getenv
import environ

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path,override=True)
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("IS_DEVELOPMENT", "True") == "True" 



  # Reading .env file

# Set ALLOWED_HOSTS
ALLOWED_HOSTS = [
    getenv("APP_HOST"),
    '127.0.0.1'
]
# ALLOWED_HOSTS += ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'blog',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
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

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER' : 'djangoblog' ,
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST' : os.getenv('DATABASE_HOST'),
        'PORT' : '5432'
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/files/"

# if DEBUG:  # Local development
#     STATIC_URL = '/static/'
#     STATICFILES_DIRS = [BASE_DIR / "static"]
#     STATIC_ROOT = BASE_DIR / "staticfiles"
#     MEDIA_ROOT = BASE_DIR / "uploads"
#     MEDIA_URL = "/files/"
# else:  # Production
#     AWS_STORAGE_BUCKET_NAME = "django-tech-blog"
#     AWS_S3_REGION_NAME = "eu-west-2"
#     AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

#     STORAGES = {
#         "default": {
#         "BACKEND": "custom_storages.MediaFileStorage",
#         },
#         "staticfiles": {
#         "BACKEND": "custom_storages.StaticFileStorage",
#         }
#     }
#     AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

#     STATICFILES_FOLDER = "static"

#     MEDIAFILES_FOLDER = "media"






EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#SendGrid username and API key
EMAIL_HOST_USER = 'apikey'  # This should always be 'apikey' for SendGrid
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')  

# Default from email
DEFAULT_FROM_EMAIL = 'techtimereply@outlook.com' 



AWS_STORAGE_BUCKET_NAME = "django-tech-blog"
AWS_S3_REGION_NAME = "eu-west-2"
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

STORAGES = {
    "default": {
        "BACKEND": "custom_storages.MediaFileStorage",
    },
    "staticfiles": {
        "BACKEND": "custom_storages.StaticFileStorage",
    }
}

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_FOLDER = "static"

MEDIAFILES_FOLDER = "media"



