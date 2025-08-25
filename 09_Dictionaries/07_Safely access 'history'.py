'''
Safely access 'history'.
Input: scores = {'math': 80, 'science': 90}
Expected Output: 'Not found'

'''
scores = {'math': 80, 'science': 90}
print(scores.get('history', 'Not found'))
