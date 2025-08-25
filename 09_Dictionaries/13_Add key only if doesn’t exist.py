'''
Add a key 'status' with value 'active' to user = {'name': 'Riya'} only if it doesn’t exist.
Input: user = {'name': 'Riya'}
Expected Output: {'name': 'Riya', 'status': 'active'}

'''
user = {'name': 'Riya'}
user.setdefault('status', 'active')
print(user)
