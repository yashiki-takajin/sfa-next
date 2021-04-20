"""
Django settings for IISE project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from os import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

PROJECT_NAME = 'SFA-Next'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]

# Application definition

INSTALLED_APPS = [
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'pure_pagination',
    'register.apps.RegisterConfig',
    'sfa',
    'social_django',
    'socials.apps.SocialsConfig',
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

ROOT_URLCONF = 'IISE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'IISE.wsgi.application'

# Circle CI用のDB設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'circle_test',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'register.pipeline.get_username',   # カスタムユーザーを使用
    'register.pipeline.create_user',    # カスタムユーザーの登録
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'register.pipeline.welcome_new_user',   # 確認メールの送信
)

# カスタムユーザーを使う
AUTH_USER_MODEL = 'register.User'
SOCIAL_AUTH_USER_MODEL = 'register.User'

# TOKEN関連
ACTIVATION_TIMEOUT_SECONDS = 60 * 60 * 24
HASH_SALT = 'SFA-Next-hash-salt'

# 新規ユーザー登録を許可する
REGISTER_NEW_USER_FLG = True

# ログインページと、直接ログインページへ行った後のリダイレクトページ
LOGIN_URL = 'register:login'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# メールをコンソールに表示する
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ソーシャル認証処理の制御用
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['registration_flg']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard/'

# Heroku用の設定とローカル設定を共存させる
DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())

    # 以下の設定はlocal_settingsもしくはHEROKUの環境変数に設定する
    # ---ここから---
    SECRET_KEY = environ['SECRET_KEY']
    
    # SOCIAL AUTH
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']
    #SOCIAL_AUTH_TWITTER_KEY = environ['SOCIAL_AUTH_TWITTER_KEY']
    #SOCIAL_AUTH_TWITTER_SECRET = environ['SOCIAL_AUTH_TWITTER_SECRET']
    #SOCIAL_AUTH_GITHUB_KEY = environ['SOCIAL_AUTH_GITHUB_KEY']
    #SOCIAL_AUTH_GITHUB_SECRET = environ['SOCIAL_AUTH_GITHUB_SECRET']
    
    # reCAPTCHA
    GOOGLE_RECAPTCHA_SITE_KEY = environ['GOOGLE_RECAPTCHA_SITE_KEY']
    GOOGLE_RECAPTCHA_SECRET_KEY = environ['GOOGLE_RECAPTCHA_SECRET_KEY']
    
    # メールサーバー接続用
    EMAIL_HOST = environ['EMAIL_HOST']
    EMAIL_PORT = environ['EMAIL_PORT']
    EMAIL_HOST_USER = environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']
    EMAIL_USE_SSL = environ['EMAIL_USE_SSL']
    # ---ここまで---
