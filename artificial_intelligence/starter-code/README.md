# Tic-T-AI-Toe

## Description
TODO: Lore

## Détails

- Le serveur (X) jouera toujours en premier. Vous (O) jouerez toujours deuxième.
- Le serveur jouera 50 parties en rafale. Vous devrez en gagner ou obtenir une partie nulle 45 fois sur 50 pour obtenir le flag.
- Le serveur envera l'état du jeu et vous devrez répondre par l'action choisie. Seulement le caractère correspondant à l'action choisie doit être retournée.
- Si une action illégale est retournée, le serveur arrête la rafale de parties.
- Un exemple de client (fonctionne sous Python 3) vous est fourni.
- Une classe permettant de reconstruire l'état du jeu vous est fournie.
- Le client a 1.0 seconde pour répondre lorsqu'un nouvel état de jeu est retourné. Si le client prend trop de temps à répondre, la rafale de parties est arrêtées.
