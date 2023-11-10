def max_subarray_2d(matrix):
    M, N = len(matrix), len(matrix[0])
    # Initialize the global maximum sum to a very small number
    max_sum = float('-inf')

    # Iterate over each column of the matrix
    for j in range(N):
        # Initialize the current column sum to zero
        current_sum = 0

        # Iterate over each row of the matrix
        for i in range(M):
            # Update the current sum by taking the maximum between the extension of the previous subarray and the current element
            current_sum = max(current_sum + matrix[i][j], matrix[i][j])
            
            # Update the global maximum sum
            max_sum = max(max_sum, current_sum)

    return max_sum

A = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

result = max_subarray_2d(A)
print("Max subarray sum:", result)
