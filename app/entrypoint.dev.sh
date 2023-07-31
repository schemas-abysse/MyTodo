#! /bin/sh

# Ce script permet de vérifier que le service de base de donnée est bien démarré au sein
# du conteneur avant d'appliquer les migrations
if [ "$DATABASE" = "postgres" ] || [ "$DATABASE" = "Postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started !"

elif [ "$DATABASE" = "mysql" ] || ["$DATABASE" = "MySQL"]
then
    echo "Waiting for MySQL..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "MySQL started !"

elif [ "$DATABASE" = "mariadb" ] || ["$DATABASE" = "MariaDB"]
then
    echo "Waiting for MariaDB..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "MariaDB started !"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"