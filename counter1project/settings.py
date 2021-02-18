"""
Django settings for counter1project project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib import messages


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8khvy%6)npzm&4@^q=#$3yn9bzilmnzc8w$lkx5*i+w5^9om=z'

# SECURITY WARNING: don't run with debug turned on in productionform!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ea55f14f2a59.ngrok.io']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'counter1app.apps.Counter1AppConfig',
    'bootstrap4',
    'import_export',    
    'rest_framework',
    'crispy_forms',
]
IMPORT_EXPORT_USE_TRANSACTIONS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'counter1project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'counter1project.wsgi.application'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sakoemmanuel4@gmail.com'
EMAIL_HOST_PASSWORD = '0725939687'



AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.github.GithubOAuth2',    

    'django.contrib.auth.backends.ModelBackend',  
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'counter1',
        'USER': 'ariso',
        'PASSWORD':'Barbie1991',
        'HOST': 'localhost',
        'PORT': ''
        
 }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True



MESSAGE_TAGS={
    messages.ERROR:'danger'
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



LOGIN_URL='login'
LOGIN_REDIRECT_URL='home'

LOGOUT_URL='logout'
LOGOUT_REDIRECT_URL='login'


# SOCIAL_AUTH_FACEBOOK_KEY	=	'319365083043094'	
# SOCIAL_AUTH_FACEBOOK_SECRET	=	'39c956013b26fa5c508f77311287996c'	


# SOCIAL_AUTH_GITHUB_KEY = 'cb36fa37ce3e11fb2eb5'      
# SOCIAL_AUTH_GITHUB_SECRET = ' c3f4eecd55c8009db3ebd5b59407872fcb5770b0 ' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
