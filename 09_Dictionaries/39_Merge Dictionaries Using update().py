'''
Merge two dictionaries into one using the update() method.

Input:

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}


Expected Output:

{'x': 1, 'y': 3, 'z': 4}

'''
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d1.update(d2)
print(d1)
