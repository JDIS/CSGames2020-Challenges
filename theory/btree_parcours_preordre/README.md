# Parcours préordre d'arbre binaire

Un parcours d'arbre consiste à explorer l'entièreté de l'arbre, noeud par noeud. Plus spécifiquement, en parcours préordre, pour chaque noeud que l'on explore, on explore ensuite ses enfants linéairement, de la gauche vers la droite. Dans le cas d'un arbre binaire, on explore l'enfant de gauche s'il existe, puis on explore l'enfant de droite s'il existe.

Votre défi consiste à décoder l'arbre contenu dans le fichier d'entrée et à en retourner le parcours préordre. À chaque noeud de l'arbre sera associé une valeur entière. La représentation du parcours préordre devra être la *concaténation* des valeurs des noeuds dans l'ordre dans lequel ils sont explorés. Le flag format `FLAG{résultat}` doit être respecté.

## Format du fichier d'entrée

Le fichier d'entrée est un fichier texte qui contient, sur chaque ligne, un noeud de l'arbre. Les noeuds sont représentés par un tuple composé des valeurs suivantes :
* La valeur du noeud
* La valeur de l'enfant gauche du noeud. Une valeur de `-1` indique que le noeud n'a pas d'enfant.
* La valeur de l'enfant droit du noeud. Une valeur de `-1` indique que le noeud n'a pas d'enfant.

Les noeuds dans le fichier sont ordonnés de façon aléatoire. Reconstruire l'arbre à partir de la liste de ses noeuds fait partie du défi.

## Exemple

Si le fichier d'entrée est le suivant :
```
(10,5,15)
(0,-1,-1)
(15,-1,-1)
(5,-1,0)
```

L'arbre correspondant est le suivant :
```
  10
 / \
5   15
 \
  0
```

Le parcours préordre est le suivant :
```
10->5->0->15
```

Et le flag est donc `FLAG{105015}`.