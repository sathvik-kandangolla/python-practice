'''Intersection of three lists
input:a = [1, 2, 3, 4]
      b = [2, 3, 5]
      c = [2, 3, 6]
expeacted output:[2,3]
'''

a = [1, 2, 3, 4]
b = [2, 3, 5]
c = [2, 3, 6]
common = list(set(a) & set(b) & set(c))
print(common)

