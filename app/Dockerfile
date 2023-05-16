# Depuis une image alpine contenant Python en version 3.11
FROM python:3.11-alpine

# On définit le dossier de travail au sein du conteneur
WORKDIR /usr/src/app

# On définit une variable d'environnement indiquant à Python qu'il ne doit pas écrire des fichier .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# On définit une variable d'environnement indiquant à Python qu'il ne doit pas charger en cacher les sorties d'output et d'erreurs
ENV PYTHONUNBUFFERED 1

# On met a jour les paquets et on installe les drivers nécessaires à Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# On upgrade pip
RUN pip install --upgrade pip
# On copie notre fichiers 'requirements.txt' vers le dossier de travail
COPY ./requirements.txt .
# On installe les modules au sein du conteneur
RUN pip install -r requirements.txt

# On copie notre dossier depuis l'hôte vers le conteneur
COPY . .