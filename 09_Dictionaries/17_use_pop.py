'''
Use .pop() to remove 'name' from info = {'name': 'Amit', 'city': 'Pune'} and print the value removed.
Input: info = {'name': 'Amit', 'city': 'Pune'}
Expected Output: Removed value = "Amit", Dictionary = {'city': 'Pune'}

'''
info = {'name': 'Amit', 'city': 'Pune'}
removed = info.pop('name')
print("Removed:", removed)
print(info)
