'''Problem: Compute the sum of each row in a matrix (list of lists).
Input:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Expected Output:

[6, 15, 24]'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sums = [sum(row) for row in matrix]
print(row_sums)   # [6, 15, 24]
