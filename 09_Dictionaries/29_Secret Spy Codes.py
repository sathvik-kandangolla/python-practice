'''
You intercepted a list of coded messages (keys), but your team uses new code names (a mapping). How will you quickly rename every code to its new secret label?
Input: codes = {'alpha': 'ok', 'beta': 'wait'}, new_labels = {'alpha': 'red', 'beta': 'blue'}
Expected Output: {'red': 'ok', 'blue': 'wait'}

'''
codes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}

renamed = {new_labels[k]: v for k, v in codes.items()}
print(renamed)
