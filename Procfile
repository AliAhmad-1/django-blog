web: gunicorn blog.wsgi --log-file - 
web: python manage.py migrate && gunicorn blog.wsgi