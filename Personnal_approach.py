import random
import time

def find_max_element(matrix):
    M, N = len(matrix), len(matrix[0])
    
    max_element = float('-inf')
    max_i, max_j = 0, 0

    for i in range(M):
        for j in range(N):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_i, max_j = i, j

    return max_i, max_j, max_element

def generate_random_submatrix(matrix, max_i, max_j):
    M, N = len(matrix), len(matrix[0])
    
    i1 = random.randint(0, max_i)
    j1 = random.randint(0, max_j)
    i2 = random.randint(max_i, M - 1)
    j2 = random.randint(max_j, N - 1)

    return i1, j1, i2, j2

def personnal(matrix, iterations):
    M, N = len(matrix), len(matrix[0])
    
    max_i, max_j, max_element = find_max_element(matrix)
    max_sum = float('-inf')
    result = None

    for x in range(iterations):  
        i1, j1, i2, j2 = generate_random_submatrix(matrix, max_i, max_j)

        current_sum = 0
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                current_sum += matrix[i][j]

        if current_sum > max_sum:
            max_sum = current_sum
            result = i1, j1, i2, j2

    return max_sum, result

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

def display_results(matrice, submatrix, start, stop, max_sum):
    
    elapsed_time = "{:.7f}".format(stop - start)

    print("Max subarray sum:", max_sum)
    print("Time to execute : ", elapsed_time, " seconds")

    for i in range(submatrix[0], submatrix[2] + 1):
        row = []
        for j in range(submatrix[1], submatrix[3] + 1):
            row.append(matrice[i][j])
        print(row)



start = time.perf_counter()
max_sum, submatrix = personnal(matrice_1,500)
stop = time.perf_counter()

display_results(matrice_1, submatrix,start, stop, max_sum)

start = time.perf_counter()
max_sum, submatrix = personnal(matrice_2,500)
stop = time.perf_counter()

display_results(matrice_2, submatrix,start, stop, max_sum)

start = time.perf_counter()
max_sum, submatrix = personnal(matrice_3,500)
stop = time.perf_counter()

display_results(matrice_3, submatrix,start, stop, max_sum)