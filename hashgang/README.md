# Hashgang

`hashes.txt` contient 2000 hash de 4 algorithmes différents.
Le contenu de ce qui a été hash est différent selon le type d'algorithme:

### MD5
Un octet d'une valeur aléatoire.

### SHA1
Une `string` de 4 caractères avec cet alphabet: `abc`

### SHA256
Une `string` de 3 caractères avec cet alphabet: `abcdefghijklmnopqrstuvwxyz`

### SHA3_512
Une `string` de 6 caractères (commençant par `0x`) avec cet alphabet: `0123456789abcdef`

Vous devez trouver le message hashé pour chaque hash. La réponse est la concaténation du premier caractère de chaque **message** hashé, en ordre.
Dans le cas de MD5, il s'agit du nombre (si on a hashé l'octet 234, on concatène 234 à la réponse. Si c'est 5, on concatène 5).

Ex: si on a hashé 'salut', 50 et 'lagang', la réponse sera 's50l'

Le calcul ne devrait aller relativement vite (pas prendre plus d'une minute).
