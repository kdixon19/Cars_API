# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i)(4l9^vn$4#5jx06puwfl=u*f^w0e^00w=cu$7lj42--i86b-'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}