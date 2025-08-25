'''
Merge three dictionaries into one.

Input:

d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'c': 3}


Expected Output:

{'a': 1, 'b': 2, 'c': 3}

'''

d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'c': 3}
merged = {**d1, **d2, **d3}
print(merged)
