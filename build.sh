#!/bin/bash

# build the project
echo "Building the project"
python3.9 -m pip install --upgrade pip

pip3 install awscli
pip3 install -r requirements.txt
pip3 --version
echo "Make Migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "collect static..."
python3.9 manage.py collectstatic --noinput --clear