import os


#################################################
# PATH Configuration
#################################################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#################################################
# Main configuration variables
#################################################
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '14qvv4rlqo^7y!kr6xkvkl$rgjttbw*$cg@n9_%6zswa4k48ih'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'test_rest_api.urls'
WSGI_APPLICATION = 'test_rest_api.wsgi.application'

ALLOWED_HOSTS = []

#################################################
# Time and Language Config
#################################################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#################################################
# File and Directory Config
#################################################
STATIC_URL = '/static/'

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

#################################################
# Account and Auth Config
#################################################
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

#################################################
# Application Config
#################################################
LOCAL_APPS = (
    'product',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

)

LAST_APP = (
    'rest_framework',
    'django_filters',

)
INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + LAST_APP

#################################################
# Middleware config
#################################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#################################################
# Database Config
#################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test_api_db',
        'USER': 'test_api_user',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
#################################################
# Framework config
#################################################
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
