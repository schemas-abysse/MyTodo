![Logo de virage conseil](https://www.virageconseil.com/wp-content/uploads/2022/01/vc.png)

# Template Django - Docker

## Sommaire
* [Description du projet](#description-du-dépôt)
* [Environnement de développement](#mise-en-place-de-lenvironnement-de-développement)
  * [Concernant les migrations](#environnement-de-développement-migrations--)

## Description du dépôt

Ce dépôt permet la mise en place rapide d'une application Django au sein d'un conteneur Docker.
\
Il offre ainsi un environnement de développement et un environnement de production grâce à l'utilisation
de différents Dockerfile et fichiers 'compose.yml'.

## Mise en place de l'environnement de développement
> :warning: Avant de commencer toute manipulation veuillez-vous déconnecter 
> de ce dépot !

### **Se déconnecter du dépôt**
````shell
git remote rm origin
````

Créez un [environnement virtuel](https://virtualenv.pypa.io/en/latest/) au sein du dossier `./app` en utilisant les commandes
mentionnées ci-dessous :
````shell
# Se placer dans le dossier ./app
cd ./app

# Créer l'environnement virtuel
python -m venv venv

# Installer les dépendances du projet
pip install -r requirements.txt
````
Ouvrez un terminal à la racine du projet puis démarrez le conteneur de développement grâce à la commande suivante :
````shell
docker compose -f compose.dev.yml up -d --build
````

### Environnement de développement, migrations : 

L'environnement de développement permet deux gestions différentes des migrations

- Les migrations sont réalisées au démarrage du conteneur
- Les migrations peuvent être réalisées manuellement 
  - Pour se faire, il est nécessaire de modifier le fichier `entrypoint.dev.sh`

````shell
#!/bin/sh

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
# Les deux lignes à commenter sont les deux lignes suivantes
python manage.py flush --no-input
python manage.py migrate

exec "$@"
````

## L'environnement de production

Cet environnement de production comporte différents services : 

| **service** | os de l'image  | version de l'image |
|:-----------:|:--------------:|:------------------:|
|  postgres   |     alpine     |         15         |
|    nginx    |     alpine     |       1.23.4       |
