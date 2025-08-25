'''
Change multiple values at once.
Input: info = {'a': 10, 'b': 20}
Expected Output: {'a': 100, 'b': 100}

'''
info = {'a': 10, 'b': 20}
info.update({'a': 100, 'b': 100})
print(info)
