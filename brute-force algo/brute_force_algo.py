
import numpy as np

def brute_force_maximum_segment_sum_2d(arr):
    M, N = len(arr), len(arr[0])
    max_sum = float('-inf')
    result = None

    for i1 in range(M):
        for i2 in range(i1, M):
            for j1 in range(N):
                for j2 in range(j1, N):
                    subarray_sum = np.sum(arr[i1:i2 + 1, j1:j2 + 1])
                    if subarray_sum > max_sum:
                        max_sum = subarray_sum
                        result = (i1, i2, j1, j2)

    return max_sum, result

def brute_force_maximum_segment_sum_constrained(arr, K, L):
    M, N = len(arr), len(arr[0])
    max_sum = float('-inf')
    result = None

    for i1 in range(M - K + 1):
        i2 = i1 + K - 1
        for j1 in range(N - L + 1):
            j2 = j1 + L - 1
            subarray_sum = np.sum(arr[i1:i2 + 1, j1:j2 + 1])
            if subarray_sum > max_sum:
                max_sum = subarray_sum
                result = (i1, i2, j1, j2)

    return max_sum, result

# Example usage:
arr = np.array([[1, 2, -1, -4, -20],
                [-8, -3, 4, 2, 1],
                [3, 8, 10, 1, 3],
                [-4, -1, 1, 7, -6]])

# Unconstrained formulation
max_sum, result = brute_force_maximum_segment_sum_2d(arr)
print(f"Maximum Sum: {max_sum}")
print(f"Indices: {result}")

# Constrained formulation with K=3, L=3
K, L = 3, 3
max_sum, result = brute_force_maximum_segment_sum_constrained(arr, K, L)
print(f"Maximum Sum (constrained): {max_sum}")
print(f"Indices (constrained): {result}")
