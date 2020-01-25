# Émulateur PSP 2
Nous sommes le 27 octobre 2034, une journée seulement avant le grand départ du Romano Fafard. En guise de bonne chance, le capitaine Charles Patenaude reçoit une boite pleine de vieux jeux vidéos pour amuser l'équipage durant leur long périple. Dans celle-ci, il découvre un classique: la version PSP de Metal Gear Solid Peace Walker! Malheureusement cette antique console n'existe plus depuis belle lurette et le capitaine vous charge donc de créer un émulateur qui lui permettra de jouer à ce petit bijoux.

Rome ne s'est pas construit........ en criant lapin, je ne boirai pas de ton eau! Alors, au travail!

## Architecture du CPU
La PSP utilise une architecture MIPS qui appartient à la famille RISC. Pour ce défi, l'achitecture simplifiée suivante sera utilisée:
- Registres
  - 4 temporary registers: `$t0`, `$t1`, `$t2`, `$t3`
  - 4 saved registers: `$s0`, `$s1`, `$s2`, `$s3`
  - 1 zero register: `$zero`
  - 1 low-order of word: `lo`
  - 1 return-value register: `$v0`
  - 1 return-address register: `$ra`
  - 1 stack-pointer register: `$sp`
  - 1 program counter: `pc`
- La RAM est supposée infinie
- Seule la `stack` sera utilisée (pas de `heap`)
- Considérez que tous les registres sont initialisés à 0
- Considérez qu'il n'y aura pas de [dépassement d'entier](https://fr.wikipedia.org/wiki/D%C3%A9passement_d%27entier)


**Afin de simplifier le travail, les addresses seront des entiers commençant à 0 et incrémentés par 1 (au lieu de 4 normalement dans une architecture 32 bits).**

## Liste des instructions
Le défi utilise une version française de l'assembleur MIPS 1998 (pour éviter la triche). Voici une [documentation](http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html) détaillée des différentes instrucstions originales.

Pour ce défi, les instructions supplémentaires suivantes devront être implémentées:
- `SAUT target`         (jump to target)
    - MIPS: `J`
    - Opération: `pc` = target
    - Description: Effectue un saut (jump) vers l'addresse de destination
- `SAUTAL target `
    - MIPS: `JAL`
    - Opération: `$ra` = `pc` + 1 et `pc` = target
    - Description: Enregistre l'addresse de retour et effectue un saut (jump) vers l'addresse de destination
- `SAUTR $s` 
    - MIPS: `JR`
    - Opération: `pc` = `$s`
    - Description:  Effectue un saut (jump) vers l'addresse de destination contenue dans le registre
- `BEQ $s $t offset`
    - MIPS: `BEQ`
    - Opération: si `$s` == `$t`, alors `pc` = `pc` + offset
    - Description: Effectue une comparaison suivi d'un saut (jump) si les valeurs des registres sont égales
- `SAUVW $t offset($s)`
    - MIPS: `SW`
    - Opération: `$($s + offset)` = `$t`
    - Description: Sauvegarde la valeur du registre `t` à un certain offset de l'addresse contenue dans le registre `s`
- `LOADW $t offset($s)`
    - MIPS: `LW`
    - Opération: `$t` = `$($s + offset)`
    - Description: Load dans le registre `t` la valeur trouvée à un certain offset de l'addresse contenue dans le registre `s`

**Pour chaque opération où le `$pc` n'est pas mentionné, vous devez l'augmenter de 1.**

## Entré et résultat attendu
Le [fichier suivant](https://pastebin.com/END5hr08) contient le programme que vous devez exécuter. Le flag est un chiffre conrespondant à l'addition des registres `$s0` à `$s3`.
