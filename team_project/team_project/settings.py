from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-14+%#$t4smbth4+%v4&$69ez^*t)+41%dw#69(5zv2r+(m1$j@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['team22-22.bham.team', '127.0.0.1', 'localhost']


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://192.168.0.25:8081",
    "http://192.168.0.25:8080",
    "https://team22-22.bham.team",
    "http://0.0.0.0:8000",
]

CORS_ORIGIN_WHITELIST = [
    "https://team22-22.bham.team",
    "http://192.168.0.25:8080",
    "http://192.168.0.25:8081",
    "http://localhost:8080",
    "http://localhost:8081",
    "https://team22-22.bham.team/register",
    "http://0.0.0.0:8000/",
]

# default_headers = [
#     'accept',
#     'accept-encoding',
# ]
# CORS_ALLOWED_HEADERS = list (default_headers) + [
#     'content-type',
# ]
CORS_ALLOW_HEADERS = ['accept',
                    'accept-encoding',
                    'authorization',
                    'content-type',
                    'dnt',
                    'origin',
                    'user-agent',
                    'x-csrftoken',
                    'x-requested-with',]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
    'forum',
    'help_section',
    'study_groups',
    'homepage',
    'dashboard',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'rest_framework_simplejwt.token_blacklist',
    'azure.storage.blob',
    'storages',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'team_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'team_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'team_project',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        # 'HOST': '',
        'HOST': 'db',
        'PORT': '5432',
        # 'PORT': '',
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

USE_I18N = True

USE_TZ = True

# CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
BASE_URL = 'http://localhost:8000'
SERVER_URL = 'https://team22-22.bham.team'

AZURE_ACCOUNT_NAME = 'teamproject'
AZURE_ACCOUNT_KEY = 'TvugZzDaTGkdgnZKQwzOsSjgdLcWongNPR433WCqOwLI+jN4GRV/R1gRUapBbbkD4VGm47QaVON0+AStdea6TA=='
AZURE_CONTAINER = 'events'
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    '/var/www/static/',
]

