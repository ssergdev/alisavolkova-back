#!/bin/sh
set -e

/wait
python manage.py makemigrations
python manage.py migrate                 
python manage.py collectstatic --noinput 

: ${MODE:='prod'}
if [ $MODE = 'prod' ]
then
    exec gunicorn app.wsgi \
        --bind 0.0.0.0:8000 \
        --workers 4 \
        --timeout 90 \
        & celery -A app worker -l info "$@"    
else
    exec python manage.py runserver 0.0.0.0:8000 --nostatic & celery -A app worker -l info "$@" 
fi
