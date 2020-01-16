# Caesar Cipher Encrypt

Le Caesar Cipher est une méthode rudimentaire d'encryption de chaines de texte.

Ses paramètres sont la chaine de texte à encrypter et une *key* correspondant à un nombre entier.

Chaque caractère dans la chaine de texte qui correspond à une lettre de l'alphabet est remplacé par la lettre située *key* positions plus loin dans l'alphabet, avec *wrap-around* (si on encrypte le caractère **z** de 1, le résultat est **a**). La casse n'est pas modifiée, ni les caractères spéciaux.

Votre défi consiste à encrypter toutes les chaines de caractère contenues dans le fichier d'entrée. Le flag correspond à la concaténation de la première lettre de chaque chaine encryptée, case sensitive, en respectant le flag format `FLAG{résultat}`.

## Format du fichier d'entrée

Le fichier d'entrée est un fichier texte qui contient, sur chaque ligne, une *key*, suivie d'un point virgule, suivi de la chaine de caractères à encrypter.

## Exemple

Si le fichier d'entrée est le suivant :
```
1;abcde
2;Hello world!
```

Le résultat de chaque encryption est :
```
bcdef
Jgnnq yqtnf!
```

Et le flag est donc `FLAG{bJ}`.