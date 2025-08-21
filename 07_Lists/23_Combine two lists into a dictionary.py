'''Combine two lists into a dictionary

Input: ['a', 'b', 'c'], [1, 2, 3]
Expected Output: {'a': 1, 'b': 2, 'c': 3}'''

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = dict(zip(keys, values))
print(result)
