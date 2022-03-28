"""
Django settings for plz project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u6-u2goiyr%8ulp2wrec93gg=+2b(rx@=y_*ym9!eqya@7w#bj'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = [] # 모두 허용


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first',
    'second',
    'main',
    'eat',
    'workout',
    'plan',
    'mypage',
    'commu',
    # 'storages', #깃헙에 올릴때 주석처리
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

ROOT_URLCONF = 'plz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'plz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# The number of seconds a password reset link is valid for (default: 3 days). 장고에서 토큰유효 기본값이 3일
PASSWORD_RESET_TIMEOUT = 60*30 #토큰 유효한 시간은 30분으로 지정

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'second.User' # Auth_user_model second앱의 user모델로 바꾼다고 알려줌.

# import os, json  #깃헙에 올릴때 주석처리
#
# # 미디어 파일을 위한 스토리지 설정
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # # # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # #
# with open(os.path.join(BASE_DIR, 'plz/secret.json')) as f:
#     secrets = json.loads(f.read())
#
# AWS_S3_REGION_NAME = 'ap-northeast-2'
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_ACCESS_KEY_ID = secrets['AWS']['Access_key_id']
# AWS_SECRET_ACCESS_KEY = secrets['AWS']['Secret_access_key']
# AWS_STORAGE_BUCKET_NAME = secrets['AWS']['Storage_bucket_name']
# AWS_DEFAULT_ACL = 'public-read' # 올린 파일을 누구나 읽을 수 있게 지정합니다!
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
#     AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME )
#
# # Media Setting
# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
#
# #email #전송용
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = secrets['MAIL']["Email_host_user"]
# EMAIL_PORT = 587
# EMAIL_HOST_PASSWORD = secrets['MAIL']["Email_host_password"]
# EMAIL_USE_TLS = True # 이거말고 일단 SSL로 시도
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# # SECURE_SSL_REDIRECT = True #reset_link 를 https로 보내주기위한 설정
#
# SECURE_SSL_REDIRECT=False
# SESSION_COOKIE_SECURE=False
# CSRF_COOKIE_SECURE=False
