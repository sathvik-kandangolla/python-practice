'''
Convert two lists into a dictionary where one list contains keys and the other contains values.

Input:

keys = ['name', 'age', 'city']
values = ['Ravi', 25, 'Delhi']


Expected Output:

{'name': 'Ravi', 'age': 25, 'city': 'Delhi'}

'''
keys = ['name', 'age', 'city']
values = ['Ravi', 25, 'Delhi']
d = dict(zip(keys, values))
print(d)
