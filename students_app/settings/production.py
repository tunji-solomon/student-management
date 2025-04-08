from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get('SECRET_KEY')