'''
Reverse the order of keys in a dictionary, so the last becomes first and vice versa.
Input: d = {'first': 1, 'second': 2, 'third': 3}
Expected Output: {'third': 3, 'second': 2, 'first': 1}

'''
d = {'first': 1, 'second': 2, 'third': 3}
reversed_dict = dict(reversed(d.items()))
print(reversed_dict)
