"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-wq*r^pki8#u#p=2$vp&r5sqee&m!#-vmrm&9ph-f9ze*nsw%ni')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '0') == '1'

# ALLOWED_HOSTS para EC2
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.amazonaws.com',
    '.compute.amazonaws.com',
    os.environ.get('SERVER_IP', ''),
    '3.23.104.9',  # Substitua pelo IP real da sua EC2
]

# CSRF - atualize com IP da sua EC2
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://3.23.104.9',  # Substitua pelo IP real da sua EC2
    'https://3.23.104.9', # Se usar HTTPS
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pontos.apps.PontosConfig',
    'django_extensions'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Adicione esta linha
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database - Configuração PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'macumbei_db',
        'USER': 'macumbei_user',
        'PASSWORD': os.environ.get('DB_PASSWORD', 'sua_senha_aqui'),
        'HOST': 'db',  # Nome do serviço no docker-compose
        'PORT': '5432',
    }
}

# Backup: se quiser manter SQLite como fallback
# DATABASES = {
#     'default': dj_database_url.config(
#         default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
#     )
# }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de segurança para produção
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True  # Mude para True se usar HTTPS
    CSRF_COOKIE_SECURE = True     # Mude para True se usar HTTPS
    
    # Se quiser usar S3 no futuro, descomente abaixo:
    # AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    # AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # AWS_DEFAULT_ACL = None
    # 
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # 
    # MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'