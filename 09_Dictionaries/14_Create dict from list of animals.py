'''
Given a list ['dog', 'cat', 'rabbit'], create a dictionary with words as keys and their lengths as values.
Input: ['dog', 'cat', 'rabbit']
Expected Output: {'dog': 3, 'cat': 3, 'rabbit': 6}

'''
animals = ['dog', 'cat', 'rabbit']
d = {a: len(a) for a in animals}
print(d)
