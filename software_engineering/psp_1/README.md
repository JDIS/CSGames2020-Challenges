# Émulateur PSP 1
Nous sommes le 27 octobre 2034, une journée seulement avant le grand départ du Romano Fafard. En guise de bonne chance, le capitaine Charles Patenaude reçoit une boite pleine de vieux jeux vidéos pour amuser l'équipage durant leur long périple. Dans celle-ci, il découvre un classique: la version PSP de Metal Gear Solid Peace Walker! Malheureusement cette antique console n'existe plus depuis belle lurette et le capitaine vous charge donc de créer un émulateur qui lui permettra de jouer à ce petit bijoux.

Rome ne s'est pas construit........ en criant lapin, je ne boirai pas de ton eau! Alors, au travail!

## Architecture du CPU
La PSP utilise une architecture MIPS qui appartient à la famille RISC. Pour ce défi, l'achitecture simplifiée suivante sera utilisée:
- Registres
  - 4 temporary registers: `$t0`, `$t1`, `$t2`, `$t3`
  - 4 saved registers: `$s0`, `$s1`, `$s2`, `$s3`
  - 1 zero register: `$zero`
  - 1 low-order of word: `lo`
- Considérez que tous les registres sont initialisés à 0
- Considérez qu'il n'y aura pas de [dépassement d'entier](https://fr.wikipedia.org/wiki/D%C3%A9passement_d%27entier)

## Liste des instructions
Le défi utilise une version française de l'assembleur MIPS 1998 (pour éviter la triche). Voici une [documentation](http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html) détaillée des différentes instrucstions originales. Cet assembleur est relativement simple, presque toutes les instructions ont le format suivant: `INSTRUCTION DESTINATION SOURCE_1 SOURCE_2`.

Pour ce défi, les instructions suivantes devront être implémentées:
- `AJOUT $d $s $t`
    - MIPS: `ADD`
    - Opération: `$d` = `$s` + `$t`
    - Description: Additionne les valeurs de deux registres et enregistre le résultat dans un autre registre
- `AJOUTI $d $s imm`
    - MIPS: `ADDI`
    - Opération: `$d` = `$s` + imm
    - Description: Additionne une valeur fixe à la valeur d'un registre et enregistre le résultat dans un autre registre
- `SOUS $d $s $t`
    - MIPS: `SUB`
    - Opération: `$d` = `$s` - `$t`
    - Description: Soustrait les valeurs de deux registres et enregistre le résultat dans un autre registre
- `MULTI $s $t`
    - MIPS: `MULT`
    - Opération: `lo` = `$s` * `$t`
    - Description: Multiplie les valeurs de deux registres et enregistre le résultat dans le registre `lo`
- `DIVI $s $t`
    - MIPS: `DIV`
    - Opération: `lo` = `$s` / `$t`
    - Description: Divise les valeurs de deux registres et enregistre le résultat dans le registre `lo`
- `BOUGELO $d`
    - MIPS: `MFLO`
    - Opération: `$d`=`lo`
    - Description: Bouge valeur du registre `lo` dans un autre registre
- `OU $d $s $t`
    - MIPS: `OR`
    - Opération: `$d` = `$s` | `$t`
    - Description: Effectue un OU entre les valeurs de deux registres et enregistre le résultat dans un autre registre
- `OUI $d $s imm`
    - MIPS: `ORI`
    - Opération: `$d` = `$s` | imm
    - Description: Effectue un OU entre une valeur fixe et la valeur d'un registre et enregistre le résultat dans un autre registre
- `ET $d $s $t`
    - MIPS: `AND`
    - Opération: `$d` = `$s` & `$t`
    - Description: Effectue un ET entre les valeurs de deux registres et enregistre le résultat dans un autre registre
- `XOR $d $s $t`
    - MIPS: `XOR`
    - Opération: `$d` = `$s` ^ `$t`
    - Description: Effectue un OU EXCLUSIF entre les valeurs de deux registres et enregistre le résultat dans un autre registre

## Entré et résultat attendu
Le [fichier suivant](https://pastebin.com/HDRgxUiP) contient le programme que vous devez exécuter. Le flag est un chiffre conrespondant à l'addition des registres `$s0` à `$s3`.