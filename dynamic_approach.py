import time

def dynamic(matrix):
    M, N = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    result = None
    for j in range(N):
        current_sum = 0
        start_row = 0
        for i in range(M):
            current_sum = max(current_sum + matrix[i][j], matrix[i][j])
            if current_sum > max_sum:
                max_sum = current_sum
                result = (start_row, j, i, j)
            if current_sum < 0:
                current_sum = 0
                start_row = i + 1 

    return max_sum, result

def display_max_submatrix(matrix, max_sum, submatrix, start_time, stop_time):
    i1, j1, i2, j2 = submatrix
    elapsed_time = "{:.7f}".format(stop_time - start_time)

    print("Somme maximale:", max_sum)
    print("Time to execute : ", elapsed_time, " seconds")
    print("Sous-matrice résultante:")

    submatrix_result = [row[j1:j2 + 1] for row in matrix[i1:i2 + 1]]
    for row in submatrix_result:
        print(row)

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
result, submatrix = dynamic(matrice_1)
stop = time.perf_counter()

display_max_submatrix(matrice_1, result, submatrix, start, stop)

start = time.perf_counter()
result, submatrix = dynamic(matrice_2)
stop = time.perf_counter()

display_max_submatrix(matrice_2, result, submatrix, start, stop)

start = time.perf_counter()
result, submatrix = dynamic(matrice_3)
stop = time.perf_counter()

display_max_submatrix(matrice_3, result, submatrix, start, stop)
