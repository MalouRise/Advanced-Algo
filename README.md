# Advanced-Algo
Cet algorithme brute-force explore systématiquement toutes les sous-matrices possibles pour trouver la sous-matrice de somme maximale.
Il effectue ces opérations : 
-On initialise la somme maximale à moins l'infini et les indices du résultat à None.
-On utilise des boucles imbriquées pour parcourir tous les indices possibles de i1, i2, j1, et j2.
-Pour chaque combinaison d'indices, on calcule la somme de la sous-matrice correspondante en utilisant la bibliothèque NumPy.
-Si une somme plus grande est trouvée, on met à jour la somme maximale et les indices du résultat.
-En fin de compte, on renvoie la somme maximale et les indices correspondant
