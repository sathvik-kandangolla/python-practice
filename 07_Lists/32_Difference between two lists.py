'''Difference between two lists
 input:a = [1, 2, 3, 4]
       b = [2, 4, 6]
       expecated output:[1,3]
'''

a = [1, 2, 3, 4]
b = [2, 4, 6]
diff = [x for x in a if x not in b]
print(diff)

