# Backend Challenge

Ce challenge vise à créer un backend HTTP simple. Il est divisé en **4** parties:

## lvl0: Créer et exposer le backend

Vous devez créer un service qui répond un message statique.
- Route: `GET /salut`
- Réponse attendue: `Salut la gang`

Vous devez exposer votre service Web afin que le serveur de correction puisse y accéder. La solution la plus simple est probablement d'utiliser [ngrok](https://ngrok.com/). Si vous avez des problèmes à le set up, venez nous voir.

## lvl1: Route dynamique

Vous devez créer une route dynamique.
- Route: `GET /salut/{mot1}/{mot2}`
- Réponse attendue: `Salut <mot1> <mot2>`

Exemples: `/salut/la/gang` devrait retourner `Salut la gang`

## lvl2: JSON

Vous devez créer une route dynamique qui retourne un objet JSON et qui utilise des GET parameters.

- Route: `GET /json`
- Paramètres GET: `debut`: un entier et `fin`: un entier supérieur ou égal à debut. Pas besoin de valider les erreurs.
- Réponse attendue: 
  - Contenu: Un objet json qui contient deux éléments: un avec la clé "Woop" et la valeur "woop". L'autre avec "suite" comme clé et une liste d'entiers de `debut` à `fin` (où `fin` est exclusif) comme valeur.
  - Un header `Content-Type: application/json`

Exemple de retour: `debut = 3` et `fin = 6`

`{"Woop": "woop", "suite": [3, 4, 5]}`

## lvl3: Persister des objets

Vous devez être en mesure de sauvegarder une `Brique`. Une brique a trois caractéristiques: un `name` (string), une `hauteur` (float) et une `largeur` (float).

- Routes:
  - `GET /brique` Retourne la liste des briques as a JSON array (avec le même header qu'au lvl2).
  - `POST /brique` Permet de sauvegarder une brique.
- Paramètres:
  - `POST /brique` prend un objet JSON comme donnée qui contiendra `name`, `hauteur` et `largeur`.
- Réponse attendue:
  - `POST /brique` doit retourner le code HTTP 201.
