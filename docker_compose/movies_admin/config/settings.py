from pathlib import Path
import os
from split_settings.tools import include
from dotenv import load_dotenv

load_dotenv()

include(
    "components/database.py",
    "components/installed_apps.py",
    "components/application_definition.py",
    "components/internationalization.py",
    "components/auth_password_validators.py",
    "components/logging.py",
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False) == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Translation management

LOCALE_PATHS = ["movies/locale"]

INTERNAL_IPS = [
    "127.0.0.1",
]


def show_toolbar(request):
    return True


if DEBUG:
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
]
