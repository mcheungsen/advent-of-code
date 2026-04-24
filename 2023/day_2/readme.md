# Cube Conundrum
## 🧩 partie 1
Somme des `id` des jeux possibles selon une quantité de couleurs pré-définis :
> only 12 red cubes, 13 green cubes, and 14 blue cubes

### Approche 1
Pour la première approche :
- Création d'un dictionnaire contenant le nombre de chaque couleur
- Tableau de `games` contenant les différents `sets`
- Chaque `set` => dictionnaire créé, pour comparer avec le dictionnaire `loaded_bag`

L'idée est de parcourir chaque set de chaque jeu, et si le set est possible, on l'additionne au résultat.

### Approche 2
Dans la première approche, je ne m'arrête que sur le set, et non sur le jeu. je continue de parcourir le jeu actuel en sachant pertinemment qu'il est faux et que je ne l'additionnerai pas au résultat. 

- For devient un while : éviter de parcourir alors qu'on a déjà la réponse

### Notes
ligne 15, création d'un dictionnaire en une seule ligne : On pouvait clairement se perdre dans ce double for en une ligne. Pas encore super habituée à la création de tableau/dictionnaire en une ligne, que je trouve d'ailleurs génial. MAIS pas encore super bien assimilé, donc j'ai mis bien plus de temps à faire ce code d'une ligne, QUE de faire en plusieurs lignes qui aurait été en fait plus rapide à écrire pour mon cas. C'était tout de même un bon entraînement pour du only one line, très sympa à faire, même si ça peut paraître illisible. à améliorer

## 🧩 partie 2
Ici, on est obligé de tout parcourir, pour trouver le minimum nombre de cubes pour chaque couleur dans un jeu.

1. On parcourt chaque set de jeu pour trouver le minimum de chaque couleur
2. On multiplie chaque nombre pour avec le `power` pour chaque jeu
3. on l'ajoute au `result` 