'''
How do you convert a frozenset back to a regular set?
input =frozenset([1, 2, 3])

Output:

{1, 2, 3}

'''
fs = frozenset([1, 2, 3])
s = set(fs)
print(s)
