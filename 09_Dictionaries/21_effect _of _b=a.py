'''
Show what happens when you do b = a with a = {'x': [1, 2]} and then modify b['x']. What happens to a?
input = a = {'x': [1, 2]} and then modify b['x'].
Expected Output: a = {'x': [1, 2, 3]}

'''
a = {'x': [1, 2]}
b = a
b['x'].append(3)
