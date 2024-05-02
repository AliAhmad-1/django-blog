#!/bin/bash

# build the project
echo "Building the project"
pip install -r requirements.txt

echo "Make Migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "collect static..."
python3.9 manage.py collectstatic --noinput --clear