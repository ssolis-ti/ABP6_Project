#!/bin/bash
set -e

# Asegurarse de que la base de datos esté lista si usamos PostgreSQL
if [ "$DATABASE" = "postgres" ]
then
    echo "Esperando por la base de datos PostgreSQL..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL ha iniciado y aceptó peticiones correctamente."
fi

# Migraciones (Quita --noinput si tienes flujos especiales en prod)
python manage.py migrate --noinput

# Archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar el CMD original definido en Dockerfile o compose
exec "$@"
