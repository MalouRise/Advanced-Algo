def max_sum_submatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    max_submatrix = None

    for i in range(rows):
        prefix_sum = [0] * cols

        for j in range(i, rows):
            for k in range(cols):
                prefix_sum[k] += matrix[j][k]
            
            current_sum = 0
            current_submatrix = []

            for k in range(cols):
                if current_sum <= 0:
                    current_sum = prefix_sum[k]
                    current_submatrix = [matrix[j][k]]
                else:
                    current_sum += prefix_sum[k]
                    current_submatrix.append(matrix[j][k])

                if current_sum > max_sum:
                    max_sum = current_sum
                    max_submatrix = current_submatrix

    return max_sum, max_submatrix

# Définissez la matrice
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

max_sum, max_submatrix = max_sum_submatrix(matrix)

print("The max sum is :", max_sum)
print("The sub-matrix with max sum is :")
for row in max_submatrix:
    print(row)
