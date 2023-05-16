![Logo de virage conseil](https://www.virageconseil.com/wp-content/uploads/2022/01/vc.png)

# Template Django - Docker

## Sommaire
* [Description du projet](#description-du-dépôt)
* [Environnement de développement](#mise-en-place-de-lenvironnement-de-développement)

## Description du dépôt

Ce dépôt permet la mise en place rapide d'une application Django au sein d'un conteneur Docker.
\
Il offre ainsi un environnement de développement et un environnement de production grâce à l'utilisation
de différents Dockerfile et fichiers 'compose.yml'.

## Mise en place de l'environnement de développement
Ouvrez un terminal à la racine du projet puis démarrez le conteneur de développement grâce à la commande suivante :
````shell
docker compose -f compose.dev.yml up -d --build
````
Connectez vous au shell du container et exécuter les migrations de base grâce à cette commande : 
````shell
docker compose exec -f compose.dev.yml wep-app python manage.py migrate --noinput
````
