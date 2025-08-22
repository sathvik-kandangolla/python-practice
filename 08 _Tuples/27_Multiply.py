'''
Multiply all numbers in tuple (2,3,4).
Remove all 2s from (1,2,2,3,4,2,5).
Output: (1, 3, 4, 5)
'''
t = (2,3,4)
product = 1
for x in t:
    product *= x
print(product)
