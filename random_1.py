import random
import time

def extract_random_submatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    if row == 0 or col == 0:
        return []

    start_row = random.randint(0, row - 1)
    start_col = random.randint(0, col - 1)

    end_row = random.randint(start_row, row - 1)
    end_col = random.randint(start_col, col - 1)

    submatrix = [row[start_col:end_col + 1] for row in matrix[start_row:end_row + 1]]

    submatrix_sum = sum(sum(row) for row in submatrix)

    return (start_row, start_col, end_row, end_col), submatrix_sum


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

def display_result(matrix, submatrix_sum, submatrix, start, stop):
    i1, i2, j1, j2 = submatrix
    elapsed_time = "{:.7f}".format(stop - start)

    print("Somme de la sous-matrice:", submatrix_sum)
    print("Time to execute : ", elapsed_time, " seconds")
    print("Sous-matrice résultante:")
    
    for row in matrix:
        print(row)

start = time.perf_counter()
submatrix, submatrix_sum = extract_random_submatrix(matrice_1)
stop = time.perf_counter()

display_result(matrice_1, submatrix_sum, submatrix, start, stop)

start = time.perf_counter()
submatrix, submatrix_sum = extract_random_submatrix(matrice_2)
stop = time.perf_counter()

display_result(matrice_2, submatrix_sum, submatrix, start, stop)

start = time.perf_counter()
submatrix, submatrix_sum = extract_random_submatrix(matrice_3)
stop = time.perf_counter()

display_result(matrice_3, submatrix_sum, submatrix, start, stop)
