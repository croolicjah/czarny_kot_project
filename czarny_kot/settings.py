"""
Django settings for czarny_kot project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import environ

from pathlib import Path

env = environ.Env(
    # set casting, default value
    # DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*', '.czarny_kot.app']

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', 'https://czornykot.pl']

SECURE_REFERRER_POLICY = 'origin'

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'czarny_kot',
    'posts',
    'tinymce',


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

ROOT_URLCONF = 'czarny_kot.urls'

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


WSGI_APPLICATION = 'czarny_kot.wsgi.app'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DATABASE"),
        "USER": env('POSTGRES_USER'),
        "PASSWORD": env('POSTGRES_PASSWORD'),
        "HOST": env("POSTGRES_HOST"),
        "URL": env("POSTGRES_URL"),
        "PORT": "5432"
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pl-PL'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]
STATICFILES_DIRS = [
    # ...
    (BASE_DIR / "static"),
]

STATIC_URL = '/static/'
STATIC_ROOT = '/var/task/ static'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/var/task/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TINYMCE_JS_URL = env('TINYMCE_JS_URL')

TINYMCE_COMPRESSOR = False

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'silver',
    'branding': False,
    # 'skin': 'oxide-dark',
    "height": "320px",
    "width": "700px",

    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor save searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": " | blocks fontfamily fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | italic underline strikethrough | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save p rint | insertfile image media pageembed template link anchor | "
    " | ",

    # 'toolbar2': '''
    #     visualblocks visualchars |
    #     charmap hr pagebreak nonbreaking anchor |  code |
    #     ''',

    'font_formats': '''
                       Arial=arial,helvetica,sans-serif; 
                       Arial Black=arial black,avant garde; 
                       Book Antiqua=book antiqua,palatino; 
                       Comic Sans MS=comic sans ms,sans-serif; 
                       Courier New=courier new,courier; 
                       Georgia=georgia,palatino; 
                       Helvetica=helvetica; 
                       Impact=impact,chicago; 
                       Symbol=symbol; 
                       Tahoma=tahoma,arial,helvetica,sans-serif; 
                       Terminal=terminal,monaco; 
                       Times New Roman=times new roman,times; 
                       Trebuchet MS=trebuchet ms,geneva; 
                       Verdana=verdana,geneva; 
                       Webdings=webdings; 
                       Wingdings=wingdings,zapf dingbats,
                   '''
}

# TINYMCE_SPELLCHECKER = True
#
# JAZZMIN_UI_TWEAKS = {
#
#     "theme": "lux",
#     # "dark_mode_theme": "darkly",

# }