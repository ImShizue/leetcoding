On vous donne un tableau d'entiers `nums` et un entier `k`.

Un entier `h` est appelé valide si toutes les valeurs du tableau qui sont strictement supérieures à `h` sont identiques.

Par exemple, si `nums = [10, 8, 10, 8]`, un entier valide est `h = 9` car tous les `nums[i] > 9` sont égaux à 10, mais 5 n'est pas un entier valide.

Vous êtes autorisé à effectuer l'opération suivante sur `nums` :

	Sélectionnez un entier `h` qui est valide pour les valeurs actuelles de `nums`.
	Pour chaque indice `i` où `nums[i] > h`, définissez `nums[i]` à `h`.

Retournez le nombre minimum d'opérations nécessaires pour rendre tous les éléments de `nums` égaux à `k`. S'il est impossible de rendre toutes les valeurs égales à `k`, retournez -1.

 

Exemple 1 :

Entrée : `nums = [5,2,5,4,5]`, `k = 2`

Sortie : 2

Explication :

Les opérations peuvent être effectuées dans l'ordre en utilisant les entiers valides 4 puis 2.

Exemple 2 :

Entrée : `nums = [2,1,2]`, `k = 2`

Sortie : -1

Explication :

Il est impossible de rendre toutes les valeurs égales à 2.

Exemple 3 :

Entrée : `nums = [9,7,5,3]`, `k = 1`

Sortie : 4

Explication :

Les opérations peuvent être effectuées en utilisant les entiers valides dans l'ordre 7, 5, 3, et 1.

 

Contraintes :

	1 <= nums.length <= 100 
	1 <= nums[i] <= 100
	1 <= k <= 100
