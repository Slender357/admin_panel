# application_definition
import os
from dotenv import load_dotenv

load_dotenv()

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "movies.apps.MoviesConfig",
    "corsheaders",
]
if os.environ.get("DEBUG", False) == "True":
    INSTALLED_APPS.append("debug_toolbar")
