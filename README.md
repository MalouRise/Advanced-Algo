# Advanced-Algo
This brute-force algorithm systematically explores all possible submatrices to find the maximum sum submatrix.
It performs these operations:

1.**Initialize** : We initialize the maximum sum to minus infinity and the indices of the result to None.

2.**Loop** : We use nested loops to traverse all possible indices of i1, i2, j1, and j2.

3.**Calculate** : For each combination of indices, we calculate the sum of the corresponding submatrix.

4.**Update** : If a larger sum is found, we update the maximum sum and the indices of the result.

5.**Return** : At the end, we return the maximum sum and the corresponding indices

**Exemple d'utilisation**

Here is an example of how to use the brute_force_maximum_segment_sum_2d function:

```python
arr = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 10, 1, 3],
       [-4, -1, 1, 7, -6]]
```

**Appel de la fonction pour la forme non contrainte**
```python
max_sum, result = brute_force_maximum_segment_sum_2d(arr)
print(f"Maximum Sum: {max_sum}")
print(f"Indices: {result}")
```
