import random

def generate_random_submatrix(matrix):
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    i1 = random.randint(0, rows)
    i2 = random.randint(i1, rows)
    j1 = random.randint(0, cols)
    j2 = random.randint(j1, cols)
    return i1, i2, j1, j2

def generate_population(pop_size, matrix):
    population = []
    for i in range (pop_size):
        random_submatrix = generate_random_submatrix(matrix)
        population.append(random_submatrix)
    return population
    

def evaluate_submatrix(matrix, submatrix):
    i1, i2, j1, j2 = submatrix
    submatrix_sum = sum(matrix[i][j] for i in range(i1, i2 + 1) for j in range(j1, j2 + 1))
    return submatrix_sum

def algorithm(matrix, population_size, generations):
    best_submatrix = None
    best_sum = float('-inf')

    for x in range(generations):
        population = generate_population(population_size, matrix)
        for submatrix in population:
            submatrix_sum = evaluate_submatrix(matrix, submatrix)
            if submatrix_sum > best_sum:
                best_sum = submatrix_sum
                best_submatrix = submatrix

    return best_sum, best_submatrix

matrix_A = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

max_sum, submatrix = algorithm(matrix_A, 100, 100)
print("Somme maximale:", max_sum)

i1, i2, j1, j2 = submatrix
print("Sous-matrice résultante:")
for i in range(i1, i2 + 1):
    row = []
    for j in range(j1, j2 + 1):
        row.append(matrix_A[i][j])
    print(row)