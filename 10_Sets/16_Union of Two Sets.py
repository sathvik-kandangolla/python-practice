'''
Union of Two Sets

Input:

A = {1, 2, 3}
B = {3, 4, 5}


Expected Output:

{1, 2, 3, 4, 5}

'''


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union of two sets
print(A | B)        # {1, 2, 3, 4, 5, 6}
print(A.union(B))   # {1, 2, 3, 4, 5, 6}
