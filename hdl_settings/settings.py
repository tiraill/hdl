import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '=#*z@+z=pnqnt$yr#q_a7dmv4@gf3x&)z#dc!ai+rd0=jpzw&7'
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'article',
    'brochure',
    'catalog',
    'education',
    'news',
    'project'
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

ROOT_URLCONF = 'hdl_settings.urls'

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

WSGI_APPLICATION = 'hdl_settings.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', 'hdl'),
        'USER': os.environ.get('DATABASE_USER', 'hdladmin'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'hdlpass'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', 5435)
    },
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'templates/static'),
    )

MEDIA_ROOT = os.path.join(BASE_DIR, 'templates/media')
MEDIA_URL = '/media/'

PRODUCT_IMAGES_ROOT = os.path.join(MEDIA_ROOT, 'images')
PRODUCT_IMAGES_URL = '/images/'

IMAGE_THUMBNAIL_HEIGHT = os.environ.get('IMAGE_THUMBNAIL_HEIGHT', 300)
IMAGE_THUMBNAIL_WIDTH = os.environ.get('IMAGE_THUMBNAIL_WIDTH', 300)
IMAGE_THUMBNAIL_SIZE = (IMAGE_THUMBNAIL_HEIGHT, IMAGE_THUMBNAIL_WIDTH)

FILE_UPLOAD_LIMIT_MULTIPLIER = os.environ.get('FILE_UPLOAD_LIMIT_MULTIPLIER', 5)
FILE_UPLOAD_LIMIT = FILE_UPLOAD_LIMIT_MULTIPLIER * 1024 * 1024  # 5 Mb

# Django email settings
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT", "465")
EMAIL_USE_SSL = True
