#!/usr/bin/env bash

DJANGO_SETTINGS_MODULE=gousto.settings.production
echo "Starting gousto"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
./manage.py migrate
./manage.py loaddata fixtures/recipe.json
exec gunicorn gousto.wsgi:application --bind 0.0.0.0:8080 --workers 3

