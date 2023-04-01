#!/usr/bin/env bash

set -e

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages -l en -l ru
python manage.py createsuperuser --no-input || true;
uwsgi --strict --ini uwsgi.ini
su web
