#!/usr/bin/env bash
set -0 errexit

pip install -r requirements.txt

python manage.py collectstatic --oninput

python manage.py migrate

python manage.py create_admin_user