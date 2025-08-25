'''
Sort a dictionary by its keys in ascending order.

Input:

d = {'banana': 3, 'apple': 5, 'cherry': 2}


Expected Output:

{'apple': 5, 'banana': 3, 'cherry': 2}

'''

d = {'banana': 3, 'apple': 5, 'cherry': 2}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)
