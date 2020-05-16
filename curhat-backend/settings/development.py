from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]
BASE_URL = "http://localhost:8000"

try:
    from .local import *
except:
    pass
