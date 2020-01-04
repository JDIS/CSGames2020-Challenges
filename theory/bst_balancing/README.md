# Balancement d'arbre binaire de recherche

Un arbre binaire de recherche est un arbre binaire dans lequel, pour un noeud donné *n* de valeur *v*, tous ses descendants à gauche ont une valeur inférieure à *v*, alors que tous ses descendants à droite ont une valeur supérieure à *v*. Ces arbres sont très utiles pour stocker et rechercher de l'information ordonnée, car le temps de recherche moyen est O(log n), contrairement à une liste chaînée par exemple, où le temps d'accès serait plutôt O(n).

On dit d'un arbre binaire de recherche qu'il est balancé si la hauteur des sous-arbres gauche et droit diffère par au plus 1, et que les sous-arbres gauche et droit sont également balancés.

Il est généralement préférable de faire en sorte qu'un arbre binaire de recherche soit balancé en tout temps (en implémentant les fonctions d'ajout et de retrait en conséquence), mais si cela n'a pas été fait, il peut-être nécessaire de balancer l'arbre entier.

Votre défi consiste à décoder l'arbre contenu dans le fichier d'entrée, à le balancer, puis à retourner le parcours préordre de l'arbre balancé. À chaque noeud de l'arbre sera associé une valeur entière. La représentation du parcours préordre devra être la *concaténation* des valeurs des noeuds dans l'ordre dans lequel ils sont explorés. Le flag format `FLAG{résultat}` doit être respecté.

## Format du fichier d'entrée

Le fichier d'entrée est un fichier texte qui contient, sur chaque ligne, un noeud de l'arbre. Les noeuds sont représentés par un tuple composé des valeurs suivantes :
* La valeur du noeud
* La valeur de l'enfant gauche du noeud. Une valeur de `-1` indique que le noeud n'a pas d'enfant.
* La valeur de l'enfant droit du noeud. Une valeur de `-1` indique que le noeud n'a pas d'enfant.

Les noeuds dans le fichier sont ordonnés de façon aléatoire. Reconstruire l'arbre à partir de la liste de ses noeuds fait partie du défi.

## Exemple

Si le fichier d'entrée est le suivant :
```
(12,7,15)
(7,5,10)
(15,-1,20)
(5,0,-1)
(10,-1,-1)
(20,-1,-1)
(0,-1,-1)
```

L'arbre correspondant est le suivant :
```
      12
     /  \
    7    15
   / \     \
  5  10     20
 /
0
```

L'arbre balancé est le suivant :
```
     10
   /   \
  5     15
 / \   /  \
0   7 12  20
```

Le parcours préordre est le suivant :
```
10->5->0->7->15->12->20
```

Et le flag est donc `FLAG{10507151220}`.