'''
Write a Python program to remove all duplicates from a list of values using a set.
input :

lst = ["a", "b", "a", "c", "b"]

Output :

['a', 'b', 'c']

'''
lst = ["a", "b", "a", "c", "b"]
lst_no_duplicates = list(set(lst))
print(lst_no_duplicates)
