# prod.py
from .base import *
import os

ALLOWED_HOSTS = [
    "0.0.0.0",
    # Curhat URL and IP
]

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "curhat",
        "USER": "postgres",
        "PASSWORD": os.environ["psqlpass"],
        "HOST": "localhost",
        "PORT": "",
    }
}
