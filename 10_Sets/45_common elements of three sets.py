'''
How do you find the common elements of three sets?
input:

a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}

Output:

{3}

'''

a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}
common = a.intersection(b, c)
print(common)
