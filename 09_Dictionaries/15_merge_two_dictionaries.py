'''
Merge two dictionaries: d1 = {'x': 1} and d2 = {'y': 2}
Input: d1 = {'x': 1}, d2 = {'y': 2}
Expected Output: {'x': 1, 'y': 2}

'''
d1 = {'x': 1}
d2 = {'y': 2}
d1.update(d2)
print(d1)
