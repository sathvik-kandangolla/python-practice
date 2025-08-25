'''
Log Session a copy of original = {'car': 'red', 'bike': 'blue'}. Change the 'car' in the copy to 'green' and print both dictionaries.
Input: original = {'car': 'red', 'bike': 'blue'}
Expected Output:original = {'car': 'red', 'bike': 'blue'}
copy = {'car': 'green', 'bike': 'blue'}

'''
original = {'car': 'red', 'bike': 'blue'}
copy = original.copy()
copy['car'] = 'green'
print(original)
print(copy)
