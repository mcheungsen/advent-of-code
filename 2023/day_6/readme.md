# Day 6 - Wait For It
## Partie 1

L'idée est de trouver le nombre de moyens de dépasser `distance` avec seulement `time`.

Au lieu de trouver TOUS les moyens, il est mieux de trouver une `range`. Ici, on va donc trouver, la vitesse minimale (temps que l'on tient le bouton), ainsi que la vitesse maximale. Ce qui fera une range des moyens possibles de dépasser la distance.

Pour trouver le `min`, on commence à la vitesse 1 et on vérifie avec le temps qu'il reste (`remain_time-vitesse`) si on dépasse le distance. On fait de même pour le max, on commence par `remain_time - 1` et on décrémente de 1 à chaque test.

## Partie 2

Ici, le temps de calcul serait énorme si l'on ne faisait pas déjà par range, car au final, ce n'est plus un tableau de temps et de distance, mais une seule distance à battre selon un seul temps imparti. On garde le même calcul de min et de max, et on trouve ainsi le résultat.