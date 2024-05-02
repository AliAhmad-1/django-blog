#!/bin/bash

# build the project
echo "Building the project"
python3.12 -m pip install -r requirements.txt

echo "Make Migrations"
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

echo "collect static..."
python3.12 manage.py collectstatic --noinput --clear