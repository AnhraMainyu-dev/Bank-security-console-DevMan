import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD')
    }
}
INSTALLED_APPS = ['datacenter']
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
