from .base import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOST")
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get('SECRET_KEY')