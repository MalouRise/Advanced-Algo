def max_subarray_2d(matrix):
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for _ in range(M)]

    # Initialize the first column of the dynamic programming matrix.
    for i in range(M):
        dp[i][0] = matrix[i][0]

    # Calculate the maximum subarray sum iteratively.
    for j in range(1, N):
        for i in range(M):
            # The maximum subarray sum ending at (i, j) depends on the previous column (j-1).
            dp[i][j] = max(dp[i][j-1] + matrix[i][j], matrix[i][j])

    # Find the global solution by selecting the maximum value from the last column of dp.
    max_sum = max(dp[i][N-1] for i in range(M))

    return max_sum

A = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

result = max_subarray_2d(A)
print("Max subarray sum:", result)
