import time

def extract_submatrix(matrix, debut, z, x, y):
    sousMatrice = []
    for i in range(debut, z + 1):
        ligne = []
        for j in range(x, y + 1):
            ligne.append(matrix[i][j])
        sousMatrice.append(ligne)
    return sousMatrice

def brute_force_maximum_segment_sum_2d(arr):
    M, N = len(arr), len(arr[0])
    max_sum = float('-inf')
    result = None 

    for i1 in range(M):
        for i2 in range(i1, M):
            for j1 in range(N):
                for j2 in range(j1, N):
                    subarray_sum = 0
                    for x in range(i1, i2 + 1):
                        for y in range(j1, j2 + 1):
                            subarray_sum += arr[x][y]
                            
                    if subarray_sum > max_sum:
                        max_sum = subarray_sum
                        result = (i1, i2, j1, j2)

    return max_sum, result


matrice_1 = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]]

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
max_sum, result = brute_force_maximum_segment_sum_2d(matrice_1)
stop = time.perf_counter()

elapsed_time = "{:.7f}".format(stop - start)

print(f"Maximum Sum: {max_sum}")
print("Time to execute : ", elapsed_time, " seconds")

sousMatrice = extract_submatrix(matrice_1, result[0], result[1], result[2], result[3])

for row in sousMatrice:
    print(row)


start = time.perf_counter()
max_sum, result = brute_force_maximum_segment_sum_2d(matrice_2)
stop = time.perf_counter()

elapsed_time = "{:.7f}".format(stop - start)

print(f"Maximum Sum: {max_sum}")
print("Time to execute : ", elapsed_time, " seconds")

sousMatrice = extract_submatrix(matrice_2, result[0], result[1], result[2], result[3])

for row in sousMatrice:
    print(row)

start = time.perf_counter()
max_sum, result = brute_force_maximum_segment_sum_2d(matrice_3)
stop = time.perf_counter()

elapsed_time = "{:.7f}".format(stop - start)

print(f"Maximum Sum: {max_sum}")
print("Time to execute : ", elapsed_time, " seconds")

sousMatrice = extract_submatrix(matrice_3, result[0], result[1], result[2], result[3])

for row in sousMatrice:
    print(row)