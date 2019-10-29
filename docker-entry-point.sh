#!/bin/sh
set -e

>&2 echo "$DATABASE_URL"
until psql $DATABASE_URL -c '\l'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done


if [ "$1" = 'gunicorn' ]; then
    >&2 echo "Executing migration"
    python manage.py migrate
fi

exec "$@"
