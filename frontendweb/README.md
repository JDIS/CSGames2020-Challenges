# Challenge Front-end JavaScript

Un serveur backend est accessible à cette addresse: SOMETHING

Ce serveur contient un endpoints pour obtenir des informations sur les pannes de service de la STM en 2019.

### GET /api/data?n=unChiffre&ligne=orange
- Retourne un objet JSON contenant une liste de unChiffre incidents paginés comme ça:
```json
{
	"current_page": 1,
	"data": [
		{
			"id": 0,
			"type": "S",
			"primaryCause": "Autres",
			"secondaryCause": "Autres",
			"symptom": "Clientèle",
			"line": "Ligne orange",
			"turnNumber": -1,
			"incidentTime": "02:56:00",
			"backToNormalTime": "03:32:00",
			"vehicle": -1,
			"doorNumber": -1,
			"equipmentType": "Non affecté",
			"locationCode": "Snowdon",
			"damagedEquipment": 0,
			"kfs": 0,
			"door": 0,
			"emergency": 0,
			"cat": 0,
			"evacuation": "-1",
			"year": 2019,
			"yearMonth": "0000-00-00",
			"monthNumber": 1,
			"dayNumber": 1,
			"weekDayNumber": 2,
			"date": "2019-01-01"
		},
		...
	],
	"first_page_url": "http://localhost:3000/api/data?page=1",
	"from": 1,
	"last_page": 432,
	"last_page_url": "http://localhost:3000/api/data?page=432",
	"next_page_url": "http://localhost:3000/api/data?page=2",
	"path": "http://localhost:3000/api/data",
	"per_page": 15,
	"prev_page_url": null,
	"to": 15,
	"total": 6468
}
```

Le paramètre "ligne" est optionnel. S'il n'est pas spécifié, toutes les lignes de métro seront retournées.

**Le challenge consiste à créer un front-end Web pour présenter ces données. Pas besoin de faire ça en ordre.**
0. Un tableau doit afficher toutes les colonnes reçues (100pts)
1. Ce tableau doit avoir un header avec le nom des colonnes en français (25pts)
2. Le tableau doit être paginé. Il doit permettre d'accéder à la première et à la dernière page, ainsi qu'à +- 3 pages de la page courante. (75pts)
3. Lorsqu'on est à la première page ou à la dernière page, le bouton première page ou dernière page est grisé, selon le cas. (25 pts)
4. S'il n'y a aucune donnée à afficher, Un message doit être inscrit au lieu du tableau. (25pts)
5. Au dessus du tableau, on peut sélectionner un bouton coloré rond selon la couleur de la ligne pour filtrer les résultats. Un indicateur entourant le rond doit permettre de savoir quelle ligne est sélectionnée. (50pts)
6. Recliquer sur le bouton sélectionné fait qu'on fetch toutes les lignes de métro. (25pts)
7. Cliquer sur un header permet de trier le tableau en ordre de cet header. Recliquer dessus fait en sorte que le tri est inversé. Une flèche permet de connaitre le sens du tri. (50 pts)
8. Au lieu d'afficher 1 ou 0, les collonnes booléennes affichent un emoji checkbox ✅ ou un emoji X rouge ❌. (25pts)
9. Un élément visuel doit permettre d'identifier qu'une requête vers le serveur est en cours. (25pts)

Il est INTERDIT d'utiliser une librairie de composantes pour faire le tableau.

La correction est manuelle. Chaque feature implémentée donne des points. Venez voir Émilio pour avoir vos points.

**Note: il est FORTEMENT recommandé d'utiliser un framework front-end (ex: Angular, React, VueJS) pour faire ce challenge.**
