# Trebuchet
## 🧩 Partie 1

> L’objectif est de parcourir chaque ligne afin de construire un nombre à deux chiffres :
>
> - le premier chiffre trouvé
> - le dernier chiffre trouvé
>
> "1" + "2" donne "12"
> vs 1 + 2 qui donne 3
### 🔍 Approche 1 — Brute force

La première idée consiste à :

1. Parcourir chaque ligne
2. Parcourir chaque caractère de la ligne
3. Vérifier si le caractère est un chiffre
4. Stocker les chiffres trouvés dans un tableau
5. Récupérer le premier et le dernier élément pour former le nombre

**Limite :** Cette méthode parcourt tous les caractères, même lorsque ce n’est pas nécessaire → approche brute-force.

### ⚡ Approche 2 — Parcours partiel

Optimisation :

- Parcourir la ligne depuis le début => s’arrêter dès qu’un chiffre est trouvé
- Parcourir la ligne depuis la fin => idem



Évite de parcourir toute la ligne
Plus efficace et plus élégant
## 🧩 Partie 2

Même principe que la partie 1, avec une contrainte supplémentaire :
> Les chiffres peuvent aussi être écrits en toutes lettres ("one", "two", etc.)

Ajout d’un dictionnaire de correspondance :

```python
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    ...
}
```

Lors du parcours :

- Si le caractère est un chiffre → on le garde
- Si c’est une lettre → on vérifie si une sous-chaîne correspond à un nombre écrit
    - Si oui → on le convertit en chiffre