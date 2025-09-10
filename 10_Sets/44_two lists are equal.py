'''
Write a Python program to check if two lists are equal (contain the same elements regardless of order).
input :

list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

Output:

True

'''

list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
print(set(list1) == set(list2))
