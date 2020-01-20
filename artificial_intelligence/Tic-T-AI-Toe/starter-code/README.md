# Tic-T-AI-Toe

## Description
Pour obtenir ce flag, vous devrez jouer jusqu'à mort s'en suive à l'infâme jeu de [Tic Tac Toe](https://www.google.com/search?q=tic+tac+toe&oq=tic+tac+toe) ! Mais pas contre n'importe qui. Contre une intelligence articielle capable de raisonner des ordres de magnitudes plus rapidement qu'un humain ! C'est maintenant votre chance de prouver que la domination des robots-tueurs n'est pas pour demain. À noter que son concepteur, débordé par sa maîtrise, n'a pas eu le temps d'implémenter un bot très bon et [qu'une stratégie très simple](https://en.wikipedia.org/wiki/Minimax) devrait l'emporter facilement.

## Détails
- Pour vous connecter: TODO: Adresse et port du serveur
- Le serveur (X) jouera toujours en premier. Vous (O) jouerez toujours deuxième.
- Le serveur jouera 50 parties en rafale. Vous devrez en gagner ou obtenir une partie nulle 45 fois sur 50 pour obtenir le flag.
- Le serveur envera l'état du jeu et vous devrez répondre par l'action choisie. Seulement le caractère correspondant à l'action choisie doit être retournée.
- Si une action illégale est retournée, le serveur arrête la rafale de parties.
- Un exemple de client (fonctionne sous Python 3) vous est fourni.
- Une classe permettant de reconstruire l'état du jeu vous est fournie.
- Le client a 1.0 seconde pour répondre lorsqu'un nouvel état de jeu est retourné. Si le client prend trop de temps à répondre, la rafale de parties est arrêtées.
