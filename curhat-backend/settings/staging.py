from .base import *
import os

ALLOWED_HOSTS = [
    "0.0.0.0",
    # Curhat Staging URL and IP
]

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "curhat_staging",
        "USER": "postgres",
        "PASSWORD": os.environ["psqlpass"],
        "HOST": "0.0.0.0",
        "PORT": "",
    }
}
