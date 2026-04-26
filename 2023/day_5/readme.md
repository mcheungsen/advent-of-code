# Day 5 - If you give a seed a fertilizer

## Partie 1

On commence par un id de graine que l'on "traduit" tout le long de chaque étape.
Ces étapes sont donnés dans l'input.

> destination - start - range

La partie 1 est facile à comprendre : On traduit chaque étape d'une `seed` jusqu'à `location`.

1. Extraire les graines de l'input : on obtient une list simple d'id de `seed`
2. Extraire chaque étape.
    - un dictionnaire d'étapes qu'on va appeler `steps_list`. 
    - une étape de cette list ordonnée sera : `nom de l'étape` : `liste des traductions`
    - cette liste de traductions, se compose de dictionnaires contenant = `destination`, `source`, `range`

> dès le moment qu'une graine entre dans une étape, et applique une "traduction", elle ne va pas en faire d'autre de cette même étape. Il ne faut pas nécessairement parcourir TOUTES les traductions, sans quoi le résultat sera faux.

3. Pour chaque `seed`, on parcourt toutes les étapes et on traduit.
    - La graine applique la traduction SI : `seed` compris entre `source` et `source + range`
    - prend pour valeur : `seed  + destination - source`
    - On récupère la `location` minimale à chaque seed parcouru à la fin.

> Pour les liste d'étapes, j'ai choisis dictionnaire pour obtenir le nom de l'étape courante. Le dictionnaire EN PYTHON est ordonné, s'il ne l'avait pas été, il aurait fallu choisir une autre méthode pour respecter l'ordre des étapes.

## Partie 2
La première ligne change : On n'a plus que deux graines, avec leur range. on a donc `seed range seed range`.

Pour la première partie, on calcule 4 graines, donc 4 localisations.
Pour la deuxième partie, on calcule beaucoup trop de graines.. Il faut donc arrêter de passer PAR GRAINE, mais PAR RANGE de graines.

La difficulté dans cette partie 2, a été que j'ai pensé par graine individuelle, et j'ai voulu faire le même calcul que la partie 1, qui me valait un temps de 5 à 9 heures de calcul. C'était clairement clairement pas la solution adaptée. l'idée de penser par range était un peu plus compliqué pour la compréhension de ma solution avant même de le coder.

On commence avec une range de graines, que l'on parcourt dans chaque étape. si une partie des graines est inclus dans l'étape, alors on divise la range de graines en deux range de graines. celle in range, et celle out of range.

Il y a deux divisions à faire : Division par la gauche, et par la droite.

### Dans l'opération ?
D'abord il faut regarder si la seed et range est dans l'opération avant de voir s'il faut diviser.

Pour mieux visualiser la graine, on passe de seed, range à min_seed, max_seed;

`min_seed = seed` et `max_seed = seed + range - 1`

> SI max >= source ET min <= source+range-1
>
> soit max_seed >= min=operation ET min_seed <= max_operation

### Division par la gauche
- Seed : 1 3 
- Operation : 3 5 

la seed commence à 1 avec une range de 3 : 1 2 et 3
L'opération commence à 3 avec une range de 5 : 3 4 5 6 7

> SI  min < min operation

Il y a un split "gauche" à faire pour cette seed : 1 et 2 ne font pas parti de l'opération actuelle. Seulement 3 fait parti de l'opération.
On divise cette seed range, en deux seeds range. Celle de gauche sera peut-être utilisé dans une autre opération!

1 3 devient => 1 2 ET 3 1 

> `seed_gauche => (seed_source, operation_source - seed_source)`
>
> `seed_center => (operation_source, seed_range - gauche_range)`

### Division par la droite

> SI max > max_operation

même principe que à gauche : on divise

> `max operation =>  source_operation + range_operation - 1`
>
> `seed_center => seed_source, (max_operation - seed_source + 1)`
>
> `seed_droite => (seed_source + center_range), (seed_range - center_range)`

Split "droite" 

### Main code

On va modifier les valeurs des seeds pour chaque opération.
Donc on commence par la première étape : 
1. Pour chaque étape, je vais parcourir toutes les seeds. J'ai donc ma seed courante.
2. Je regarde toutes les opérations. (dès que j'applique une opération je break sur les opérations pour éviter de faire plusieurs opérations pour une même étape)
3. Je trouve l'opération à faire. je récupère donc ces valeurs : destination, source, range
4. On vérifie si on doit Split la seed. (gauche ou droite ou les deux)
5. Pour les seeds out of range : on ajoute à la liste des seeds. On fera l'opération à la fin. La taille des seeds augmente : il ne faut pas boucler sur les seeds, mais boucler sur la taille du tableau des seeds pour que le tableau soit FLEXIBLE sur le parcours.
6. On fait le calcul de l'opération pour la seed actuelle et on passe à la suite.

ces étapes faites, on boucle sur les autres étapes et les autres seeds.

Dans la premiere partie, pour une graine, on faisait TOUTES les opérations. Maintenant, pour la partie 2, pour une opération, on modifie chaque rangée de graines pas à pas.

On se perd facilement dans le compréhension des calculs, j'ai donc décidé de faire des variables compréhensibles (surtout pour moi qui ai du mal à visualiser par range, j'ai ajouté des variables de min et max pour mes seeds).