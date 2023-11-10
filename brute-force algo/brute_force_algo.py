def brute_force_maximum_segment_sum_2d(arr):
    M, N = len(arr), len(arr[0])
    max_sum = float('-inf')  # Initialisation de la somme maximale à moins l'infini
    result = None  # Initialisation des indices du résultat à None

    # Parcours de tous les indices i1, i2, j1 et j2 possibles
    for i1 in range(M):
        for i2 in range(i1, M):
            for j1 in range(N):
                for j2 in range(j1, N):
                    # Calcul de la somme de la sous-matrice sans utiliser NumPy
                    subarray_sum = 0
                    for x in range(i1, i2 + 1):
                        for y in range(j1, j2 + 1):
                            subarray_sum += arr[x][y]
                    
                    # Mise à jour de la somme maximale et des indices si une somme plus grande est trouvée
                    if subarray_sum > max_sum:
                        max_sum = subarray_sum
                        result = (i1, i2, j1, j2)

    return max_sum, result

# Exemple d'utilisation
arr = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 10, 1, 3],
       [-4, -1, 1, 7, -6]]

# Appel de la fonction pour la forme non contrainte
max_sum, result = brute_force_maximum_segment_sum_2d(arr)
print(f"Maximum Sum: {max_sum}")
print(f"Indices: {result}")
