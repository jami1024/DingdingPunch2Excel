import os
import environ

ROOT_DIR = (
        environ.Path(__file__) - 3
)  # get root of the project

env = environ.Env(
    DEBUG=(bool, True),
    DJANGO_DEBUG=(bool, True),
    DJANGO_LOG_LEVEL=(str, 'DEBUG'),
    DJANGO_LOG_FILE_LEVEL=(str, 'INFO'),
)

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE or env.str("PROJECT_ENV", "local"):
    # OS environment variables take precedence over variables from .env
    DOT_ENV_FILE = env.str("PROJECT_ENV", default='local')
    env.read_env(
        str(ROOT_DIR.path('.envs/.{}/.django.env'.format(DOT_ENV_FILE)))
    )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-b7&#r8((836yzya_hz@70$8=%-+*yf4k$@5&)ns+b=if(wmc66"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG")

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TWO_PARTY_APPS = [
    # 'gunicorn',
    'rest_framework',
    'django_filters',
    'corsheaders',
    # 'channels',
]

LOCAL_APPS = [
]

INSTALLED_APPS = DJANGO_APPS + TWO_PARTY_APPS + LOCAL_APPS
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 用于跨域设置
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_WHITELIS = ('*')
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'DingdingPunch2Excel.urls'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env.str("DJANGO_DB_NAME", ''),
#         'USER': env.str("DJANGO_DB_USER", ''),
#         'PASSWORD': env.str("DJANGO_DB_PASSWORD", ''),
#         'HOST': env.str("DJANGO_DB_HOST", '127.0.0.1'),
#         'PORT': env.int("DJANGO_DB_PORT", 3306),
#         'OPTIONS': {
#             'charset': env.str("DJANGO_DB_CHARSET", 'utf8mb4'),
#             # 'read_default_file': env.str("DJANGO_DB_READ_DEFAULT_FILE", '/etc/my.cnf'),
#         },
#     }
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': 'mydatabase',
#     # }
# }

# print("ssss", env.str('DJANGO_DB_ENGINE'))

if env.str("DJANGO_DB_ENGINE") == "sqlite":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    pass

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'DingdingPunch2Excel.wsgi.application'
# ASGI_APPLICATION = 'DingdingPunch2Excel.routing.application'


# DRF的设置
REST_FRAMEWORK = {
    # "PAGE_SIZE": 20,
    #"DEFAULT_PAGINATION_CLASS":"rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PAGINATION_CLASS":"utils.pagination.MyPageNumberPagination",
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 控制权限
        # 'rest_framework.permissions.AllowAny',
        'utils.permissions.Permissions',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
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
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/www/www/static/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

