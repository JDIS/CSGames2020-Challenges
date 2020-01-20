# The most important challenge of them all
## Règles
Pour résoudre ce problème, vous devez parcourir un [graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) et
trouver le chemin le plus court entre deux noeuds donnés. Pour un même poids, un
**chemin avec moins de noeud doit être favorisé**.

À la fin, vous devez imprimer chaque noeud visité en ordre. Votre liste doit inclure le noeud initial et le noeud final.
Les noeuds sont indiqués par des chiffres commençants à 0 et terminant au nombre de noeuds moins 1.

Les arcs sont définis par la source, la destination et le prix de déplacement. À noter, les arcs sont
**unidirectionnels**.

## Intéraction avec la plateforme
### Inputs
**Ligne 1**: Le noeud de départ et le noeud d'arrivée

**Ligne N**: Les arcs (source destination coût).

### Output
Le flag est la concaténation de la sortie de tous les graphes un après l'autre, donné à un algorithme de hashage MD5, dans le format `JDIS-{CONTENT_GOES_HERE}`

Exemple de flag:
Sorties de tous les grapes concaténés: 010120123
Flag: `JDIS-{a9190890aa32e36357384bc106b201b0}`

### Exemple
**Input**
```
0
3
0 1 2
1 2 4
1 3 5
2 3 3
```
**Output**
```
013
```


