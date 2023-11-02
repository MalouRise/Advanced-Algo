# Advanced-Algo 
# Branch and Bound

## Overview

The Branch and Bound Algorithm for Maximum Sum Submatrix is a Python implementation designed to find the submatrix within a given matrix that has the maximum sum of its elements. This algorithm is based on the Branch and Bound technique, which efficiently explores submatrix possibilities to find the optimal solution.

## How it Works

The Branch and Bound Algorithm applies the following steps:

1. **Initialize variables:** The algorithm initializes variables to keep track of the maximum sum and the corresponding submatrix:

    ```python
    max_sum = float('-inf')
    max_submatrix = None
    ```

2. **Exploration using Branch and Bound:** It explores submatrices using the Branch and Bound approach, which divides the search space into smaller subproblems. The algorithm efficiently prunes branches that cannot lead to a better solution.

3. **Find the maximum sum submatrix:** By exploring the search space and applying pruning techniques, the algorithm identifies the submatrix with the maximum sum.

4. **Return the results:** The algorithm returns the maximum sum and the corresponding submatrix.

## Example

Here is an example of how to use the `max_sum_submatrix` function:

```python
# Define the matrix
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

# Find the maximum sum submatrix
max_sum, max_submatrix = max_sum_submatrix(matrix)

# Print the results
print("The max sum is:", max_sum)
print("The sub-matrix with max sum is:")
for row in max_submatrix:
    print(row)

