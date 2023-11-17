import random

matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

def extract_random_submatrix(matrix, start_row, end_row, start_col, end_col):
 
    row = len(matrix)
    col = len(matrix[1])

    start_row = random.randint(0, row - 1)
    start_col = random.randint(0, col - 1)

    end_row = random.randint(start_row, row - 1)
    end_col = random.randint(start_col, col - 1)

    return [row[start_col:end_col+1] for row in matrix[start_row:end_row+1]]

submatrix = extract_random_submatrix(matrix, 1, 2, 2, 3)

for row in submatrix:
    print(row)