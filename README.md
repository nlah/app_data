# Python
version 3.5.3

## Installing Libraries

pip3 install -r requirements.txt

## Run server

python3 manage.py runserver

## Run celery start

python3 manage.py celery_start

## Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1',
            'PORT': '3306'
        }
    }

    BROKER_URL = 'amqp://guest:guest@localhost:5672//'

