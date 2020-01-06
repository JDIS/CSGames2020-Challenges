# Blockchainz
Le but de ce challenge est d'analyser le block bitcoin core (https://bitcoin.org/en/developer-reference) disponible dans block.dat au format binaire. Vous pouvez utiliser la librairie ou le site web de votre choix pour vous aider.

## Level 0
Le premier flag est simplement le nonce du block. Soumettez votre flag dans le format printf("FLAG{%i}", nonce).

## Level 1
Calculez la somme des *locktimes* de chacune des transactions. Soumettez votre flag dans le format printf("FLAG{%i}", somme).
