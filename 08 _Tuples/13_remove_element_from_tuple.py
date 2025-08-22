'''
Description: Remove a specific element from a tuple by converting it to a list and back.
Removing elements from tuples is a common interview question testing immutability handling.
Input: t = (1, 2, 3, 4), Remove: 2
Output: (1, 3, 4)

'''
t = (1, 2, 3, 4)
t = tuple(x for x in t if x != 2)
print(t)
