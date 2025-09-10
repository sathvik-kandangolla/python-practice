'''
Write a Python program to update a set with the symmetric difference of itself and another set.
input :

A = {1, 2, 3}
B = {3, 4, 5}



Output:

{1, 2, 4, 5}

'''
A = {1, 2, 3}
B = {3, 4, 5}
A.symmetric_difference_update(B)
print(A)
