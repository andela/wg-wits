#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wger.settings_global import *
from decouple import config
import dj_database_url
import os

# Use 'DEBUG = True' to get more details for server errors
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True

ADMINS = (
    (os.environ.get('ADMIN_NAME'), os.environ.get('ADMIN_EMAIL')),
)
MANAGERS = ADMINS

if os.environ.get("DB") == 'postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('WGER_NAME') or 'wger',
            'USER': os.environ.get('WGER_USER') or 'postgres',
            'PASSWORD': os.environ.get('WGER_PASSWORD') or '',
            'HOST': os.environ.get('WGER_HOST') or 'localhost',
            'PORT': os.environ.get('WGER_PORT') or '',
        }
    }

if os.environ.get("DB") == "heroku":
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL'))
    }

# Your reCaptcha keys
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
NOCAPTCHA = True

# The site's URL (e.g. http://www.my-local-gym.com or http://localhost:8000)
# This is needed for uploaded files and images (exercise images, etc.) to be
# properly served.
SITE_URL = 'http://localhost:8000'

# Path to uploaded files
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = ''
MEDIA_URL = '/media/'

# Allow all hosts to access the application. Change if used in production.
ALLOWED_HOSTS = '*'

# This might be a good idea if you setup memcached
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Configure a real backend in production
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sender address used for sent emails
WGER_SETTINGS['EMAIL_FROM'] = 'wger Workout Manager <wger@example.com>'

# Your twitter handle, if you have one for this instance.
#WGER_SETTINGS['TWITTER'] = ''
