# Problème des Deux Sommes

## Énoncé du Problème

Étant donné un tableau d'entiers `nums` et un entier `target`, retournez **les indices des deux nombres** tels que leur somme soit égale à `target`.

Vous pouvez supposer que chaque entrée a **exactement une solution**, et vous ne pouvez pas utiliser deux fois le même élément.

Vous pouvez retourner la réponse dans **n'importe quel ordre**.

---

## Exemples

### Exemple 1 :
**Entrée :**  
`nums = [2,7,11,15]`, `target = 9`  
**Sortie :**  
`[0,1]`  
**Explication :**  
Puisque `nums[0] + nums[1] == 9`, nous retournons `[0, 1]`.

---

### Exemple 2 :
**Entrée :**  
`nums = [3,2,4]`, `target = 6`  
**Sortie :**  
`[1,2]`

---

### Exemple 3 :
**Entrée :**  
`nums = [3,3]`, `target = 6`  
**Sortie :**  
`[0,1]`

---

## Contraintes

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Une seule réponse valide existe.

---

## Suivi

Pouvez-vous proposer un algorithme avec une complexité inférieure à **O(n²)** ?

---

## Solution

L'algorithme utilise un dictionnaire (`num_map`) pour stocker les compléments nécessaires et leurs indices.  
Pour chaque élément dans `nums`, nous calculons le complément (`target - num`) et vérifions s'il est déjà dans le dictionnaire.  
Si oui, nous retournons les indices correspondants. Sinon, nous ajoutons l'élément actuel et son index au dictionnaire.  

### Complexité
- **Temps :** O(n), où n est la taille de `nums`, car nous parcourons le tableau une seule fois.
- **Espace :** O(n), pour stocker les éléments dans le dictionnaire.