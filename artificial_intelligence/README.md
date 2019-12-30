# AI Challenge

## Principe

Les participants ('O') devront battre ou avoir un jeu nul contre le server ('X') 45/50. 

Le serveur joue toujours en premier.

Le serveur envoie le tableau de jeu formatté pour affichage avec chaque case numérotée, les cases jouées ayant le 'X' ou le 'O'

Le joueur doit répondre par le charactère associé à la case seulement. Si une case déjà jouée est choisie, le serveur termine la session.

Lorsqu'une partie se termine, le serveur envoie le win/total ratio au joueur et recommence la partie. Après que toutes les parties soient jouées, le serveur envoie ou non le flag.

## Setup

Pour rouler le serveur:
```
   $ python server/Server.py 127.0.0.1 65432
```
où `localhost` et `65432` sont des exemples d'hôtes et de port respectivement

Pour rouler le client de test:

```
   $ python client/Client.py
```

Qui a l'hôte et le port hardcodés


## Déploiement

Lors de la journée, le code contenu dans `client/Client.py` et dans `game/GameState.py` sera fourni pour sauver du temps aux participants
