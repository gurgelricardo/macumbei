#!/bin/sh

echo "Aplicando migrações do banco de dados..."
python manage.py migrate

echo "Iniciando o servidor Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:10000