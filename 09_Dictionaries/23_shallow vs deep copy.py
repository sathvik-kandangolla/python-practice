'''
Explain (with code) the difference between a shallow copy and a deep copy using a nested dictionary. Show the effect of changing an inner list.
Input:d = {'x': [1, 2]}
Expected Output:

shallow affects d

deep remains independent

'''
import copy
d = {'x': [1, 2]}
shallow = d.copy()
deep = copy.deepcopy(d)
shallow['x'].append(3)
