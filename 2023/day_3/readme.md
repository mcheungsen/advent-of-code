# Gear Ratios

## partie 1 - En cours

1. Parcourir chaque caractère et identifier un symbole
2. si symbole => Récupérer les indexes des nombres voisins
3. Pour chaque index, identifier le nombre complet. Supprimer des indexes pour éviter d'avoir des nombres répétés
4. Additionner le résultat

### Récupération des indexes

Au lieu de direct récupérer les nombres, on récupère les indexes voisins des symboles. On peut visualiser ce parcourt de voisins, d'une matrice de -1 à 1. Par rapport à l'index symbole, il faut regarder de -1 à +
```
| 7 | . | . |
| . | * | . |
| 3 | 5 | . |
```

on voit ici que le `7` est à (-1,-1) par rapport à `*`.
ainsi `3 => (1,-1)` et `5 => (1,0)` si on considère que `*` est à (0,0).

### Identifier le nombre complet

Pour identifier le nombre complet, à partir du premier tuple de mes indexes, je recule de 1 jusqu'à ce que ce ne soit plus un nombre. On obtient l'index de départ. Avec cet index, on incrémente de 1, et on ajoute le nombre, jusqu'à ne plus avoir de nombre.

Lorsque je rencontre un tuple déjà présent dans mes indexes, je le supprime. Je répète cette étape, jusqu'à ce que mon tableau des indexes soit vide.