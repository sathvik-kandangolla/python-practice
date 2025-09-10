'''
Write a Python program to update a set with the intersection of itself and another set.

input :

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


Output:

{3, 4}

'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.intersection_update(B)
print(A)
