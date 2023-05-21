#! /bin/sh

# Ce script permet de vérifier que le service de base de donnée est bien démarré au sein
# du conteneur avant d'appliquer les migrations
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"