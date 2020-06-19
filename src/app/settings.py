import os
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

# PATHS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'app/static')]

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=[])


# APPLICATION DEFINITION
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_filters',
    'djcelery_email',
    'rest_framework',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'parler',
    'adminsortable2',
    'ckeditor',
    'ckeditor_uploader',
    'core',
    'blocks',
    'gallery',
    'hero',
    'events',
    'workshops',
    'merch',
    'feedback',
    'django_cleanup.apps.CleanupConfig'# it should be the last item!
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ForceInRussianMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app/templates')],
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

WSGI_APPLICATION = 'app.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='postgres'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASSWORD', default=''),
        'HOST': env('DB_HOST', default='postgres'),
        'PORT': env('DB_PORT', default='5432'),
    },
}

# PASSWORD VALIDATION
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

# INTERNATIONALIZATION
LANGUAGE_CODE = 'ru'
ADMIN_LANGUAGE_CODE = 'ru'
LANGUAGE_COOKIE_NAME = 'locale'
LANGUAGES = (
    ('ru', "Russian"),
    ('en', "English"),
)

PARLER_SHOW_EXCLUDED_LANGUAGE_TABS = False
PARLER_DEFAULT_LANGUAGE_CODE = 'ru'
PARLER_LANGUAGES = {
    None: (
        {'code': 'ru', },
        {'code': 'en', },
    ),
    'default': {
        'fallbacks': ['ru'],
        'hide_untranslated': False,
    }
}

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# EASY THUMBNAILS
THUMBNAIL_HIGH_RESOLUTION = False
THUMBNAIL_SUBDIR = 'thumbs'
THUMBNAIL_QUALITY = 85
THUMBNAIL_OPTIMIZE_COMMAND = {
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}',
    'png': '/usr/bin/optipng {filename}'
}

# UPLOAD
MAX_UPLOAD_SIZE = "5242880"

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO'
        },
    },
}

# EMAIL
SITE_EMAIL = env('EMAIL_ADDR')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_REPLY_TO = env('EMAIL_REPLY_TO')
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

# CELERY
CELERY_BROKER_URL = 'redis://redis:6379/'
CELERY_RESULT_BACKEND = 'redis://redis:6379/'

# CKEDITOR
CKEDITOR_UPLOAD_PATH = 'editor/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 85

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline',
                'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink'],
            ['Image', 'Embed', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Source', 'Maximize']
        ],
        "extraPlugins": ",".join(["image2", "embed", "autoembed" ]),
        "removePlugins": ",".join(["image", "stylesheetparser"]),
        "contentsCss": "/static/admin/css/ckeditor_custom.css",
        'height': 291,
        'width': 835,
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
    }

}
