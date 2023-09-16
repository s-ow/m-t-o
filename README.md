# Météo
Je voulais à la base faire ce projet uniquement en python, mais finalement, pour pouvoir réaliser une interface graphique
plus pratique et esthétique (fond, images...), j'ai décidé de me lancer dans le JavaScript (et encore ce projet ne requiert pas un
niveau très avancé) afin de pouvoir créer un site, dont l'esthétique est très simple à manipuler pour moi.

![](https://i.imgur.com/hrcsjSv.png)

## Fonctionnement pratique
> API

Les données sont récupérées grâce à l'API gratuite de [openweathermap](https://openweathermap.org/).
Je ne possède aucun abonnement à cette api donc les requêtes sont limitées et seule la météo instatanée est utilisable.
Le temps de mise à jour des données est de 3 heures.

> Fonds

Les images de fond changeant en fonction de la météo du lieu choisi sont des images que j'ai trouvées et mises dans les assets.
J'ai simplement fait en sorte que selon le temps renvoyé par l'API, telle ou telle image apparaisse.

## Utilisation
- Utilisation du site :
> Il vous suffit de cliquer sur [le lien du site](https://s-ow.github.io/meteo) et de rechercher une ville.
> Rien de plus simple !

- Utilisation du python :
> Pour télécharger facilement les fichiers python, j'ai créé une branche qui contient uniquement les fichiers python [ici](https://github.com/s-ow/meteo/tree/python).

Une fois les fichiers installés, il vous suffit de lancer le fichier `install.bat` lors du premier lancement, puis le fichier `start.bat` par la suite.
