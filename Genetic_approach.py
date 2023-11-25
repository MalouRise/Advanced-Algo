import random
import numpy as np

def generate_pheromones_matrix(shape):
    return np.ones(shape)

def aco_max_subarray(array, iterations=100, ants=10, evaporation_rate=0.1):
    shape = np.shape(array)
    pheromones = generate_pheromones_matrix(shape)
    best_solution = None
    best_sum = float('-inf')

    for _ in range(iterations):
        for ant in range(ants):
            current_solution = []
            current_sum = 0

            # Déplacer la fourmi à travers la grille
            i, j = random.randint(0, shape[0] - 1), random.randint(0, shape[1] - 1)

            while i < shape[0] and j < shape[1]:
                current_solution.append((i, j))
                current_sum += array[i][j]


            if current_sum > best_sum:
                best_sum = current_sum
                best_solution = current_solution

        # Évaporation des phéromones
        pheromones *= (1 - evaporation_rate)

        # Mise à jour des phéromones sur la meilleure solution
        for i, j in best_solution:
            pheromones[i][j] += 1.0 / best_sum

    return best_solution, best_sum




matrix_A = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
best_path, best_sum = aco_max_subarray(matrix_A)



print("Best Subarray Path:", best_path)
print("Best Subarray Sum:", best_sum)
