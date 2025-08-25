''''
Find the key with the maximum value.

Input:

d = {'apple': 50, 'banana': 80, 'cherry': 40}


Expected Output:

banana

'''
d = {'apple': 50, 'banana': 80, 'cherry': 40}
max_key = max(d, key=d.get)
print(max_key)
