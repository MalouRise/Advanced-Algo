import time

def max_sum_submatrix_branch_and_bound(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    max_submatrix = None

    def calculate_sum(submatrix):
        return sum(sum(row) for row in submatrix)

    def branch_and_bound_submatrix(row_start, row_end, col_start, col_end):
        nonlocal max_sum, max_submatrix
        current_submatrix = [row[col_start:col_end + 1] for row in matrix[row_start:row_end + 1]]
        current_sum = calculate_sum(current_submatrix)

        if current_sum > max_sum:
            max_sum = current_sum
            max_submatrix = current_submatrix

        if col_end < cols - 1:
            # Explore right
            right_col = col_end + 1
            branch_and_bound_submatrix(row_start, row_end, col_start, right_col)
            if current_sum > max_sum:
                branch_and_bound_submatrix(row_start, row_end, right_col, col_end)

        if row_end < rows - 1:
            # Explore down
            down_row = row_end + 1
            branch_and_bound_submatrix(row_start, down_row, col_start, col_end)
            if current_sum > max_sum:
                branch_and_bound_submatrix(down_row, row_end, col_start, col_end)

    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    branch_and_bound_submatrix(r_start, r_end, c_start, c_end)

    return max_sum, max_submatrix

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
max_sum, max_submatrix = max_sum_submatrix_branch_and_bound(matrice_1)
stop = time.perf_counter()

elapsed_time = "{:.7f}".format(stop - start)

print("Max sum is :", max_sum)
print("Time to execute : ", elapsed_time, " seconds")
print("Biggest sub-matrix is :")
for row in max_submatrix:
    print(row)

    start = time.perf_counter()
max_sum, max_submatrix = max_sum_submatrix_branch_and_bound(matrice_2)
stop = time.perf_counter()

elapsed_time = "{:.7f}".format(stop - start)

print("Max sum is :", max_sum)
print("Time to execute : ", elapsed_time, " seconds")
print("Biggest sub-matrix is :")
for row in max_submatrix:
    print(row)


start = time.perf_counter()
max_sum, max_submatrix = max_sum_submatrix_branch_and_bound(matrice_3)
stop = time.perf_counter()

elapsed_time = "{:.7f}".format(stop - start)

print("Max sum is :", max_sum)
print("Time to execute : ", elapsed_time, " seconds")
print("Biggest sub-matrix is :")
for row in max_submatrix:
    print(row)

