#!/bin/bash

# Script para facilitar o deploy na EC2

echo "=== Iniciando deploy ==="

# Parar containers existentes
docker-compose down

# Build e up dos containers
docker-compose up -d --build

# Aguardar PostgreSQL ficar pronto
echo "Aguardando PostgreSQL..."
sleep 10

# Executar migrations
docker-compose exec web python manage.py migrate

# Criar superusuário (opcional)
# docker-compose exec web python manage.py createsuperuser --noinput

echo "=== Deploy concluído! ==="
