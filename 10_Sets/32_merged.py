'''
How do you merge three sets into one using a set operation?
a = {1, 2}
b = {3, 4}
c = {5, 6}

Output:

{1, 2, 3, 4, 5, 6}

'''

a = {1, 2}
b = {3, 4}
c = {5, 6}
merged = a.union(b, c)
print(merged)
