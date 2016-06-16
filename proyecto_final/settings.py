# -*- encoding: utf-8 -*-
"""
Django settings for proyecto_final project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=v648sy3ackb$u=9a07ou1*enjvmr4w^*cbkxhnnwkftr9u)9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'proyecto_final.aficionado',
    'proyecto_final.muro',
    'proyecto_final.evento',
    # Apps para Django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'datetimewidget',
    # Apps para Django-cities-light
    'cities_light',
    # Apps para Django-autocomplete-light
    'dal',
    'dal_select2',
    # Apps para Django-avatar
    'avatar',
    # Apps para Django-embed-video
    'embed_video',
    # Apps para Django-debug-toolbar
    # 'debug_toolbar',
    # Django EL(Endless) Pagination
    'el_pagination',
    # Django location field
    'location_field.apps.DefaultConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'proyecto_final.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'proyecto_final', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
                # allauth specific context processors
                # "allauth.account.context_processors.account",
                # "allauth.socialaccount.context_processors.socialaccount",
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_final.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'proyecto_final', 'uploads')

# Le indicamos donde están los elementos que metemos en la carpeta statics
# del proyecto
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'proyecto_final', 'statics')]

PAGINATION_PAGES = 20

# Cosas para django-allauth

ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_LOGOUT_REDIRECT_URL (=”/”)

# Requerido por django.contrib.sites
SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
     {'METHOD': 'oauth2',
      'SCOPE': ['email', 'public_profile', 'user_friends'],
      'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
      'VERIFIED_EMAIL': True,
      # 'LOCALE_FUNC':  lambda request: 'es-ES',
      'VERSION': 'v2.4'},

     'google':
        {'SCOPE': ['profile', 'email'],
         'AUTH_PARAMS': {'access_type': 'online'}}
     }

# Fin cosas para django-allauth

# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'set_required': False,
    'error_css_class': 'bootstrap3-error',
    'required_css_class': 'bootstrap3-required',
    'javascript_in_head': True,
}

# Settings for django-cities-light
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['es']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['ES', 'FR', 'UK']
CITIES_LIGHT_INCLUDE_CITY_TYPES = [
    'PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT', ]

CITIES_LIGHT_APP_NAME = 'aficionado'

# Settings for django-avatar
AVATAR_GRAVATAR_DEFAULT = 'http://icons.iconarchive.com/icons/graphicloads/100-flat/256/contact-icon.png'

LOCATION_FIELD_PATH = STATIC_URL + 'location_field'


LOCATION_FIELD = {
    'map.provider': 'google',
    # 'map.provider': 'openstreetmap',
    'map.zoom': 13,

    'search.provider': 'google',
    'search.suffix': '',

    # Google
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': '',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',

    # Mapbox
    'provider.mapbox.access_token': '',
    'provider.mapbox.max_zoom': 18,
    'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 18,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': [
            LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
            LOCATION_FIELD_PATH + '/js/form.js',
        ],
    },
}
