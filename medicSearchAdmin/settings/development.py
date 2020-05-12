from .settings import *

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'ADICIONE UMA HASH AQUI'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
