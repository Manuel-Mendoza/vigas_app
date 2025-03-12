import os
import dj_database_url
from corsheaders.defaults import default_methods
from corsheaders.defaults import default_headers
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

# Replace the DATABASES section of your settings.py with this


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-9u%7zlw#1g6ehgcvf+=x9=$dp%jx57ctcxwvj991ns2*^7!v3x')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
RAILWAY_DOMAIN = os.environ.get('vigasapp-production.up.railway.app', '')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.railway.app','https://vigasapp-production.up.railway.app/admin/login/?next=/admin/', RAILWAY_DOMAIN]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'rest_framework',
    'drf_spectacular',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# Configuración de drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Vigas API',
    'DESCRIPTION': 'API para gestionar órdenes y vigas',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_vigas.urls'

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

WSGI_APPLICATION = 'app_vigas.wsgi.application'

# Database
database_url = os.getenv("DATABASE_URL")
if database_url:
    tmpPostgres = urlparse(database_url)
    # Asegurarse de que path sea una cadena antes de usar replace
    db_name = tmpPostgres.path.replace('/', '') if isinstance(tmpPostgres.path, str) else tmpPostgres.path.decode().replace('/', '')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_name,
            'USER': tmpPostgres.username,
            'PASSWORD': tmpPostgres.password,
            'HOST': tmpPostgres.hostname,
            'PORT': 5432,
        }
    }

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
 # Añade esto a tu settings.py
if RAILWAY_DOMAIN:
    CSRF_TRUSTED_ORIGINS = [f'https://{RAILWAY_DOMAIN}']
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'