'''
Organize a scrambled dictionary by key order so that the output is sorted by key.
Input: d = {'b': 2, 'a': 1, 'c': 3}
Expected Output: [('a', 1), ('b', 2), ('c', 3)]

'''
d = {'b': 2, 'a': 1, 'c': 3}
print(sorted(d.items()))
