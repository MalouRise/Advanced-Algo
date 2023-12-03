import random
import time

def display_max_submatrix(matrix, max_sum, submatrix, start_time, stop_time):
    i1, i2, j1, j2 = submatrix
    elapsed_time = "{:.7f}".format(stop_time - start_time)

    print("Somme maximale:", max_sum)
    print("Time to execute : ", elapsed_time, " seconds")
    print("Sous-matrice résultante:")
    
    for i in range(i1, i2 + 1):
        row = []
        for j in range(j1, j2 + 1):
            row.append(matrix[i][j])
        print(row)


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

def genetic(matrix, population_size, generations):
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

matrice_1 = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

matrice_2 = [
    [1, 2, -1, -4, -20, 5, 3, 2, 7, 8],
    [-8, -3, 4, 2, 1, 9, 6, -2, 1, 0],
    [3, 8, 10, 1, 3, -40, 7, 5, 1, 2],
    [-4, -1, 1, 7, -6, 0, 3, -9, 6, 4],
    [2, -7, 5, 8, 2, -1, 4, -3, 2, 1],
    [-6, 3, -2, 1, 5, 7, 0, 2, -8, -3],
    [4, 2, -50, 6, 3, 1, 9, -2, 0, 8],
    [0, 1, -3, 9, 4, 2, -7, 6, 1, -5],
    [-2, 4, 6, -1, 0, 8, -3, 7, -4, 2],
    [5, 7, -8, 2, 1, -4, 6, 3, -5, -1]
]

matrice_3 = [
    [1, -20, 3],
    [4, 5, 6],
    [7, 8, 9]
]

start = time.perf_counter()
max_sum, submatrix = genetic(matrice_1, 100, 100)
stop = time.perf_counter()

display_max_submatrix(matrice_1, max_sum, submatrix, start, stop)

start = time.perf_counter()
max_sum, submatrix = genetic(matrice_2, 100, 100)
stop = time.perf_counter()

display_max_submatrix(matrice_2, max_sum, submatrix, start, stop)

start = time.perf_counter()
max_sum, submatrix = genetic(matrice_3, 100, 100)
stop = time.perf_counter()

display_max_submatrix(matrice_3, max_sum, submatrix, start, stop)